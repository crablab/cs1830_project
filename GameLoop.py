from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_fps
import pygame
import random
import copy
import time
from collections import namedtuple
from Transfer import JsonToObject
import json

from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Player import Player


from Classes.KeyHandler import keydown, keyup
from Classes.ClickHandler import checkClick

from Classes.Settings import CANVAS_WIDTH, CANVAS_HEIGHT
from Classes.Objects import cam, player_list, particle_set_middle,particle_set_top,particle_set_bottom, spriteDictionary


#-----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()


# -----INTERACTIONS?
class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line


#--------------GAME-----LOOP
def draw(canvas):

    fps.draw_fct(canvas)

#-----CAM---UPDATE---
    cam.zoom()
    cam.move()
#----CLICK---HANDLER---
    checkClick()

#-----OBJECT---UPDATES-----
    for player in player_list:
        player.update()
    for p in particle_set_top:
        p.update()
    for p in particle_set_middle:
        p.update()
    for p in particle_set_bottom:
        p.update()


#  --------DRAW---OBJECTS---BY---LAYER---PRIORITY

    for pbot in particle_set_bottom:

        pbot.draw(canvas,cam,spriteDictionary)

    for pmid in particle_set_middle:
        pmid.draw(canvas, cam, spriteDictionary)

    for ptop in particle_set_top:
        ptop.draw(canvas, cam, spriteDictionary)


    for player in player_list:
        player.draw(canvas, cam, spriteDictionary)

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



frame = simpleguics2pygame.create_frame('Game', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
