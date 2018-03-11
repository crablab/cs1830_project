#    mmm   mmmm  mmm     mmmm   mmmm   mmmm
#  m"   " #"   "   #    #    # "   "# m"  "m
#  #      "#mmm    #    "mmmm"   mmm" #  m #
#  #          "#   #    #   "#     "# #    #
#   "mmm" "mmm#" mm#mm  "#mmm" "mmm#"  #mm#

#LOADING LIBRARIES
import queue, threading, time, pycurl, json, io, sys, pygame, random, copy, configparser
from flask import Flask, request, Response
from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_fps
from collections import namedtuple

#LOADING SETTINGS
from Classes.Settings import *
config = configparser.ConfigParser()
#Open file as writeable
config.read_file(open('Classes/config'))


#Override settings when testing (to make it easier to run multiple instances)
if(len(sys.argv) > 1):
    print("OVERIDING SETTINGS_________________________")
    config['NETWORKING']['CONFIG_TYPE'] = sys.argv[1]

    config.set('NETWORKING', 'CONFIG_TYPE', sys.argv[1])
    with open('Classes/config', "w") as conf:

        config.write(conf) 

#reopen
#config.read_file(open('Classes/config'))

#LOAD INTERNAL CLASSES
from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Player import Player
from Collisions.Collisions import doCirclesIntersect
from Transfer.comms import communicate, recieve, ping
from Classes.KeyHandler import keydown, keyup
from Classes.ClickHandler import checkClick

from Classes.Objects import *
from Loops.intro import introLoop, waitingLoop


#-----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()
oldTime=time.time()

#--------------GAME-----LOOP-------------------
def draw(canvas):
    #
#-----------------CLIENT PING-----------------------
    if (config['NETWORKING']['CONFIG_TYPE'] == 'client'):
        ping()
#-----------RECIEVE ALL OBJECTS-------------------------
    recieve()
#-----------------SEND GAME STATES------------------------
    communicate(gameState1)

    if(gameState1.intro):
        print("intro")
        introLoop(canvas)
    if gameState1.main and not gameState2.main:
        print("waiting")
        waitingLoop(canvas)
    if(gameState1.main and gameState2.main):
        # print("game")

        #Threading for adding to queues
        def movingSetSend():
            global moving_set
        for object in moving_set:
            communicate(object)
        for monster in monster_set:
            communicate(monster)

        #we don't to thread this as it is a small set
        for player in player_list:
            if player.idObject==playerId:
                #print(player.particle.vel)
                communicate(player)
        # print("size:"+str(moving_set_external.__len__()))



    #-----CAM---UPDATE---
        cam.zoom()
        cam.move(playerId,player_list)
    #----CLICK---HANDLER---
        checkClick()

    #  -------UPDATE-AND-DRAW---OBJECTS---BY---LAYER---PRIORITY
    #------------place all objects into list to choose which to draw first, not sure if this is expensive, but we shall try-----------

        for pbot in env_l1_set:
            pbot.update()
            pbot.draw(canvas,cam)

        for en2 in env_l2_list:
            for pm in moving_set:
                if not pm.updated:
                    if doCirclesIntersect(pm, en2):
                        pm.draw(canvas, cam)
                        pm.update()
                        pm.updated=True

            for pe in moving_set_external:
                #print(pe.pos)
                if not pe.updated:
                    if  doCirclesIntersect(pe,en2):
                        pe.update()
                        pe.draw(canvas,cam)
                        pe.updated=True
            for m in monster_set_external:
                #print(pe.pos)
                if not m.particle.updated:
                    if   doCirclesIntersect(m.particle, en2):
                        m.draw(canvas,cam)
                        m.update()
                        m.particle.updated=True
            for m in monster_set:
                #print(pe.pos)
                if not m.particle.updated:
                    if doCirclesIntersect(m.particle, en2) and m.particle.radius<2*en2.radius:#big monsters drawn on top for simplicity ( flying ones e.t.c.)
                        m.update()
                        m.draw(canvas,cam)
                        m.particle.updated=True
            for player in player_list:

                if not player.particle.updated:
                    # print(player.particle.radius)
                    # print(player.particle.pos.getY())

                    if doCirclesIntersect(player.particle, en2):

                        player.update()
                        player.draw(canvas,cam)
                        player.particle.updated=True


            en2.update()
            en2.draw(canvas, cam)
# UPDATE those left then reset updates for all

        for p in moving_set:
            if not p.updated:
                p.draw(canvas,cam)
                p.update()
            p.updated=False
        for p in moving_set_external:
            if not p.updated:
                p.draw(canvas,cam)
                p.update()
            p.updated=False
        for pm in monster_set_external:
            if not pm.updated:
                pm.draw(canvas,cam)
                pm.update()
            pm.updated=False
        for pm in monster_set:
            if not pm.particle.updated:
                pm.draw(canvas,cam)
                pm.update()
            pm.particle.updated=False
        for pp in player_list:


            if pp.idObject==playerId:
                cam.origin=pp.particle.pos.copy()

            if not pp.particle.updated:

                pp.draw(canvas,cam)
                pp.update()
            pp.particle.updated=False

        fps.draw_fct(canvas)
    #--------COLLECT----MARKED---OBJECTS------------
        removal_set=set()


        for particle in moving_set:
            if particle.pos == particle.nextPos and particle.removeOnVelocity0:
                removal_set.add(particle)
            if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
                removal_set.add(particle)
        moving_set.difference_update(removal_set)
        removal_set.clear()

        for particle in moving_set_external:
            if particle.pos == particle.nextPos and particle.removeOnVelocity0:
                removal_set.add(particle)
            if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
                removal_set.add(particle)

        moving_set_external.difference_update(removal_set)
        removal_set.clear()

        for monster in monster_set_external:
            if monster.particle.pos == monster.particle.nextPos and monster.particle.removeOnVelocity0:
                removal_set.add(monster)
            if monster.particle.spriteSheet.hasLooped and monster.particle.removeOnAnimationLoop:
                removal_set.add(monster)

        monster_set_external.difference_update(removal_set)
        removal_set.clear()
        for monster in monster_set:
            if monster.particle.pos == monster.particle.nextPos and monster.particle.removeOnVelocity0:
                removal_set.add(monster)
            if monster.particle.spriteSheet.hasLooped and monster.particle.removeOnAnimationLoop:
                removal_set.add(monster)

        monster_set.difference_update(removal_set)
        removal_set.clear()


frame = simpleguics2pygame.create_frame('Game', int(config['CANVAS']['CANVAS_WIDTH']), int(config['CANVAS']['CANVAS_HEIGHT']))
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()