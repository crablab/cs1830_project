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
if(config['DEVELOPER']['DEVELOPER_OPTIONS'] and len(sys.argv) > 1): 
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

from Transfer.comms import communicate, recieve, ping
from Classes.KeyHandler import keydown, keyup
from Classes.ClickHandler import checkClick


from Classes.Objects import cam, particle_set_middle,particle_set_top,particle_set_bottom, spriteDictionary, moving_set,moving_set_external,player_list,playerId


#-----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()
oldTime=time.time()

#--------------GAME-----LOOP-------------------
def draw(canvas):
    #if(DEVELOPER_OPTIONS): print("External list length: " + str(moving_set_external.__len__()))
    
    #if we're a client make sure we Ping
    if(config['NETWORKING']['CONFIG_TYPE'] == 'client'):
        ping()

    #Threading for adding to queues
    def movingSetSend():
        global moving_set
    for object in moving_set:
        communicate(object)

    #we don't to thread this as it is a small set
    for player in player_list:
        if player.idObject==playerId:
            #print(player.particle.vel)
            communicate(player)
    # print("size:"+str(moving_set_external.__len__()))
    
    recieve()

#-----CAM---UPDATE---
    cam.zoom()
    cam.move()
#----CLICK---HANDLER---
    checkClick()

#  -------UPDATE-AND-DRAW---OBJECTS---BY---LAYER---PRIORITY

    for pbot in particle_set_bottom:
        pbot.update()
        pbot.draw(canvas,cam)

    for pmid in particle_set_middle:
        pmid.update()
        pmid.draw(canvas, cam)

    for ptop in particle_set_top:
        ptop.update()
        ptop.draw(canvas, cam)

    for pm in moving_set:
        pm.update()
        pm.draw(canvas,cam)

    for pe in moving_set_external:
        #print(pe.pos)
        pe.update()
        pe.draw(canvas,cam)

    for player in player_list:

        player.update()
        player.draw(canvas,cam)

    fps.draw_fct(canvas)
#--------COLLECT----MARKED---OBJECTS------------
    removal_set=set()

    for particle in particle_set_top:
        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)
    particle_set_top.difference_update(removal_set)
    removal_set.clear()

    for particle in particle_set_middle:
        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)
    particle_set_middle.difference_update(removal_set)
    removal_set.clear()

    for particle in particle_set_bottom:
        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)
    particle_set_bottom.difference_update(removal_set)
    removal_set.clear()
    
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


frame = simpleguics2pygame.create_frame('Game', int(config['CANVAS']['CANVAS_WIDTH']), int(config['CANVAS']['CANVAS_HEIGHT']))
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()