from Classes.Settings import *
from Classes.Vector import Vector

from Classes.Camera import Camera
from Classes.Mouse import Mouse

from Classes.SpriteAnimator import SpriteAnimator
from Classes.Player import Player
from Classes.Particle import Particle

import os
import random



# ---------------------ANY SETS/LISTS-----------------------

particle_set_bottom = set()
particle_set_middle = set()
particle_set_top = set()
player_list = []





#------------------ DICTIONARY OF ALL PICTURES LOCATIONS-----------------

cwd = os.getcwd()
elf_demo = SpriteAnimator(cwd + '/img/character/elf/demo.jpg')
orc = SpriteAnimator(cwd + '/img/character/elf/orc.jpg')
arrow = SpriteAnimator(cwd + '/img/character/elf/arrow.jpg')
grass01 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
grass02 = SpriteAnimator(cwd + '/img/grass/grass02.jpg')
grass03 = SpriteAnimator(cwd + '/img/grass/grass03.jpg')
grass04 = SpriteAnimator(cwd + '/img/grass/grass04.jpg')

spriteDictionary = {"elf_demo": elf_demo,"orc":orc, "grass01": grass01, "grass02": grass02, "grass03": grass04, 'arrow': arrow,
                    "grass04": grass04}






# -----------------------MOVING OBJECTS-------------------

#CAMERA
cam = Camera(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))

#PLAYER
player = Player(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y),
                Vector(PLAYER_INITIAL_VELOCITY_X, PLAYER_INITIAL_VELOCITY_Y), PLAYER_INITIAL_ANGLE,
                Vector(PLAYER_DIMENSIONS_X, PLAYER_DIMENSIONS_Y), PLAYER_RADIUS, PLAYER_SPRITE,spriteDictionary, PLAYER_ID)
player.setSpriteState(3)
player_list.append(player)

#MOUSE HANDLER (PYGAME)(NO RIGHT/MIDDLE CLICKS ON SIMPLEGUI)
mouse = Mouse()
# CONVERSION OF SIMPLE GUI MOUSE LOCATION TO PYGAME LOCATION
adjustment = Vector(250, 25)






# -----------------------NON-MOVING OBJECTS------------------

#GRASS
x = 0
for i in range(0, 100):
    if i % 10 == 0:
        x += 1
    g = Particle(Vector(x * 500, (i % 10) * 500), Vector(0, 0), 0, Vector(500, 500), 30, 'grass02',spriteDictionary, 0, 0, False,
                 False )
    g.spriteSheet.setRow(1, 1, 1, 1, 1)
    particle_set_bottom.add(g)
