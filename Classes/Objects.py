from Classes.Settings import *
from Classes.Vector import Vector

from Classes.Camera import Camera
from Classes.Mouse import Mouse

from Classes.SpriteAnimator import SpriteAnimator
from Classes.Player import Player
from Classes.Particle import Particle

import os
import random

# simple gui to Pygame click adjustment Vector:
adjustment = Vector(250, 25)

# declare sets/lists
particle_set = set()
player_list = []

# Sprites Jpg's
cwd = os.getcwd()
elf_demo = SpriteAnimator(cwd + '/img/character/elf/demo.jpg')
arrow = SpriteAnimator(cwd + '/img/character/elf/arrow.jpg')
grass01 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
grass02 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
grass03 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
grass04 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')

spriteDictionary = {"elf_demo": elf_demo, "grass01": grass01, "grass02": grass02, "grass03": grass04, 'arrow': arrow,
                    "grass04": grass04}

# initiate non-statics
cam = Camera(Vector(250, 250), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))
player = Player(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y),
                Vector(PLAYER_INITIAL_VELOCITY_X, PLAYER_INITIAL_VELOCITY_Y), PLAYER_INITIAL_ANGLE,
                Vector(PLAYER_DIMENSIONS_X, PLAYER_DIMENSIONS_Y), PLAYER_RADIUS, PLAYER_SPRITE, PLAYER_ID)

player.setSpriteState(3)
player_list.append(player)
mouse = Mouse()

# initiate statics
x = 0
for i in range(0, 100):
    if i % 10 == 0:
        x += 1

    g = Particle(Vector(x * 500, (i % 10) * 500), Vector(0, 0), 0, Vector(500, 500), 30, 'grass01', 0, 0, False,
                 False, )
    g.sprite.setRow(1, 1, 1, 1, 1)
    particle_set.add(g)
