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
from Classes.Objects import cam, player_list, particle_set, spriteDictionary


# initiate time
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()


# interactions (if required later):
class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line


# Game loop

def draw(canvas):

    fps.draw_fct(canvas)

    # adjust camera
    cam.zoom()
    cam.move()

    # updates
    checkClick()

    for player in player_list:
        player.update()



    for p in particle_set:
        p.update()
    # copy and draw Background Sprites/objects

    # copy and draw Forground Sprites/objects

    for particle in particle_set:
        p = copy.deepcopy(particle)
        p.pos.transformToCam(cam)
        p.draw(canvas,cam,spriteDictionary)

    for player in player_list:
        p = copy.deepcopy(player)
        p.particle.pos.transformToCam(cam)
        p.draw(canvas, cam, spriteDictionary)

    #collect Garbage:
    removal_set=set()
    for particle in particle_set:

        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.sprite.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)

    particle_set.difference_update(removal_set)
    removal_set.clear()

frame = simpleguics2pygame.create_frame('Game', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
