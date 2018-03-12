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
from Classes.MonsterAi import MonsterAi

#-----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()
oldTime=time.time()

#initiate Ai
monsterAi=MonsterAi(20)
monsterAi.spawnMonsters()



#--------------GAME-----LOOP-------------------
def draw(canvas):

#========== GAME LOOPS NON MAIN =====================

    if(gameState1.intro):
        print("intro")
        introLoop(canvas)

    if gameState1.main and not gameState2.main:
        print("waiting")
        waitingLoop(canvas)


#================= NETWORKING ==============================

#-----------------CLIENT PING-----------------------
    if (config['NETWORKING']['CONFIG_TYPE'] == 'client'):
        ping()
#--------------RECIEVE ALL OBJECTS-------------------------
    recieve()
#-----------------SEND GAME STATES------------------------
    communicate(gameState1)


    if(gameState1.main and gameState2.main):

#-----------IN MAIN LOOP NETWORKING-------------------------
        #Threading for adding to queues

        for object in weapon_set:
            communicate(object)
        for monster in monster_set:
            communicate(monster)
        for object in visual_set:
            communicate(object)

        #we don't to thread this as it is a small set
        for player in player_list:
            if player.idObject==playerId:
                #print(player.particle.vel)
                communicate(player)
        # print("size:"+str(moving_set_external.__len__()))

#================ NETWORKING END ================================

#===================================================================

#================ CLICK HANDLER =================================

        checkClick()

#================ CLICK HANDLER END =================================

#===================================================================

#================ DRAW AND UPDATES =================================

    #  -------UPDATE-AND-DRAW---OBJECTS---BY---LAYER---PRIORITY
        monsterAi.update()
        for pbot in env_l1_set:
            pbot.update()
            pbot.draw(canvas,cam)
        for pbot in env_l3_list:
            pbot.update()
            pbot.draw(canvas,cam)
        for v in visual_set:
            v.update()
            v.draw(canvas,cam)
        for ve in visual_set_external:
            ve.update()
            ve.draw(canvas,cam)

        # ------------place all objects into list to choose which to draw first, not sure if this is expensive, but we shall try-----------
        for en2 in env_l2_list:
            for w in weapon_set:
                if not w.particle.updated:
                    if doCirclesIntersect(w.particle, en2):
                        w.draw(canvas, cam)
                        w.update()
                        w.particle.updated=True
            for w in weapon_set_external:
                if not w.particle.updated:
                    if  doCirclesIntersect(w.particle,en2):
                        w.update()
                        w.draw(canvas,cam)
                        w.updated=True

            for m in monster_set_external:
                if not m.particle.updated:
                    if   doCirclesIntersect(m.particle, en2):
                        m.draw(canvas,cam)
                        m.update()
                        m.particle.updated=True
            for m in monster_set:
                if not m.particle.updated:
                    if doCirclesIntersect(m.particle, en2) and m.particle.radius<2*en2.radius:#big monsters drawn on top for simplicity ( flying ones e.t.c.)
                        m.update()
                        m.draw(canvas,cam)
                        m.particle.updated=True

            for player in player_list:
                if not player.particle.updated:
                    if doCirclesIntersect(player.particle, en2):
                        player.update()
                        player.draw(canvas,cam)
                        player.particle.updated=True


            en2.update()
            en2.draw(canvas, cam)

        # UPDATE those left then reset updates for all
        for w in weapon_set:
            if not w.particle.updated:
                w.draw(canvas,cam)
                w.update()
            w.particle.updated=False
        for w in weapon_set_external:
            if not w.particle.updated:
                w.draw(canvas,cam)
                w.update()
            w.particle.updated=False

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
            # if pp.idObject==playerId:
            #     cam.origin=pp.particle.pos.copy()

            if not pp.particle.updated:

                pp.draw(canvas,cam)
                pp.update()
            pp.particle.updated=False

        fps.draw_fct(canvas)
#====================== UPDATES DRAWING END =============================================

#========================================================================================

# ===================== GARBAGE REMOVAL =================================================
        removal_set=set()

        #WEAPON CLEANUP (MAGIC, ARROWS)
        for weapon in weapon_set:

            if weapon.particle.pos == weapon.particle.nextPos and weapon.particle.removeOnVelocity0:
                removal_set.add(weapon)
            if weapon.particle.spriteSheet.hasLooped and weapon.particle.removeOnAnimationLoop:
                removal_set.add(weapon)
        weapon_set.difference_update(removal_set)
        removal_set.clear()

        for weapon in weapon_set_external:
            if weapon.particle.pos == weapon.particle.nextPos and weapon.particle.removeOnVelocity0:
                removal_set.add(weapon)
            if weapon.particle.spriteSheet.hasLooped and weapon.particle.removeOnAnimationLoop:
                removal_set.add(weapon)
        weapon_set_external.difference_update(removal_set)
        removal_set.clear()

        #MONSTER_CLEANUP
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

        #VISUAL SET CLEANUP
        for v in visual_set:
            if v.pos == v.nextPos and v.removeOnVelocity0:
                removal_set.add(v)
            if v.spriteSheet.hasLooped and v.removeOnAnimationLoop:
                removal_set.add(v)
        visual_set.difference_update(removal_set)
        removal_set.clear()

        for v in visual_set_external:
            if v.pos == v.nextPos and v.removeOnVelocity0:
                removal_set.add(v)
            if v.spriteSheet.hasLooped and v.removeOnAnimationLoop:
                removal_set.add(v)
        visual_set_external.difference_update(removal_set)
        removal_set.clear()

# ========================= GARBAGE REMOVAL END ===============================================================

 # ========================================================================================

#  ======================== CAMERA UPDATE ===============================================================

        cam.zoom()
        cam.move(playerId, player_list)

# ========================== CAMERA UPDATE END==============================================================

# ========================================================================================

# ========================== STATS DISPLAY ==============================================================

        #DISPLAY STATS:
        for player in player_list:
            if player.idObject==playerId:
                p1Life=player.life
                p1Magic=player.magic
                p1Range=player.range

                p1Arrows=1
                p1Spells=(p1Magic//3000+3)*2
                if p1Range > 1000:
                    p1Arrows=2
                if p1Range > 10000:
                    p1Arrows=3

                if p1Range > 50000:
                    p1Arrows=4

        canvas.draw_text('Life: '+str(p1Life)+"     Magic: "+str(p1Magic)+"     Range: "+str(p1Range)+"     Arrows: "+str(p1Arrows)+"  Spells: "+str(p1Spells), (0,int(config['CANVAS']['CANVAS_HEIGHT'])-10), 23, "Black")

frame = simpleguics2pygame.create_frame('Game', int(config['CANVAS']['CANVAS_WIDTH']), int(config['CANVAS']['CANVAS_HEIGHT']))
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()