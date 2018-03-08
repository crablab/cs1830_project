#    mmm   mmmm  mmm     mmmm   mmmm   mmmm
#  m"   " #"   "   #    #    # "   "# m"  "m
#  #      "#mmm    #    "mmmm"   mmm" #  m #
#  #          "#   #    #   "#     "# #    #
#   "mmm" "mmm#" mm#mm  "#mmm" "mmm#"  #mm#
# Networking class


import queue, threading, time, pycurl, json, io
from flask import Flask, request, Response

from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_fps
import pygame
import random
import copy
import time
from collections import namedtuple
import json

from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Player import Player

from Transfer.comms import communicatePlayer
from Classes.KeyHandler import keydown, keyup
from Classes.ClickHandler import checkClick

from Classes.Settings import *
from Classes.Objects import cam, particle_set_middle,particle_set_top,particle_set_bottom, spriteDictionary, moving_set,moving_set_external,player_list,playerId


#-----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()





oldTime=time.time()
#--------------GAME-----LOOP-------------------
def draw(canvas):
    for player in player_list:
        if player.idObject==playerId:
            #print(player.particle.vel)
            communicatePlayer(player)


#-----CAM---UPDATE---
    cam.zoom()
    cam.move()
#----CLICK---HANDLER---
    checkClick()

#  -------UPDATE-AND-DRAW---OBJECTS---BY---LAYER---PRIORITY

    for pbot in particle_set_bottom:
        pbot.update()
        pbot.draw(canvas,cam,spriteDictionary)

    for pmid in particle_set_middle:
        pmid.update()
        pmid.draw(canvas, cam, spriteDictionary)

    for ptop in particle_set_top:
        ptop.update()
        ptop.draw(canvas, cam, spriteDictionary)

    for pm in moving_set:
        pm.update()
        pm.draw(canvas,cam,spriteDictionary)

    for pe in moving_set_external:
        pe.update()
        pe.draw(canvas,cam,spriteDictionary)

    for player in player_list:

        player.update()
        player.draw(canvas,cam,spriteDictionary)

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
        if particle.remove:
            removal_set.add(particle)
    moving_set.difference_update(removal_set)
    removal_set.clear()
    for particle in moving_set_external:
        if particle.remove:
            removal_set.add(particle)
    moving_set_external.difference_update(removal_set)
    removal_set.clear()

frame = simpleguics2pygame.create_frame('Game', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()