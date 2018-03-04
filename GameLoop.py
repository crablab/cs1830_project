from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_fps
import pygame

from collections import namedtuple
from Transfer import JsonToObject
import json

from Classes.Camera import Camera
from Classes.Grass import Grass
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Player import Player
from Classes.Settings import CANVAS_WIDTH, CANVAS_HEIGHT
from Classes.Objects import cam, grass_list, player_list, particle_set
from Classes.KeyHandler import keydown, keyup
from Classes.ClickHandler import checkClick

import random
import copy
import time

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


    for particle in particle_set:
        particle.update()
    # copy and draw Background Sprites/objects
    for grass in grass_list:
        g1 = copy.deepcopy(grass)

        g1.pos.transformToCam(cam)
        g1.draw(canvas,cam)

    # copy and draw Forground Sprites/objects
    for player in player_list:
        p = copy.deepcopy(player)
        p.pos.transformToCam(cam)
        p.draw(canvas,cam,1)

    for particle in particle_set:
        p = copy.deepcopy(particle)
        p.pos.transformToCam(cam)
        p.draw(canvas,cam)


frame = simpleguics2pygame.create_frame('A convex polygon domain', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
