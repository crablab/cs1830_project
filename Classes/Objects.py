from Classes.Settings import *
from Classes.Vector import Vector

from Classes.Camera import Camera
from Classes.Mouse import Mouse

from Classes.SpriteAnimator import SpriteAnimator
from Classes.Player import Player
from Classes.Particle import Particle

import SimpleGUICS2Pygame
from SimpleGUICS2Pygame import simpleguics2pygame
import os
import random


# ---------------------ANY SETS/LISTS-----------------------
moving_set = set()
particle_set_bottom = set()
particle_set_middle = set()
particle_set_top = set()
player_list = []

# ------------------ DICTIONARY OF ALL PICTURES LOCATIONS-----------------

cwd = os.getcwd()
elf_demo = SpriteAnimator(cwd + '/img/character/elf/demo.jpg')
orc = SpriteAnimator(cwd + '/img/character/elf/orc.jpg')
arrow = SpriteAnimator(cwd + '/img/character/elf/arrow.jpg')
whiteDragon=SpriteAnimator(cwd+'/img/character/monsters/whiteDragon.jpg')
greenDragon=SpriteAnimator(cwd+'/img/character/monsters/greenDragon.jpg')
grass01 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
water = SpriteAnimator(cwd + '/img/Water/water.jpg')
dog = SpriteAnimator(cwd + '/img/character/animals/dog.jpg')
grass02 = SpriteAnimator(cwd + '/img/grass/grass02.jpg')
grass03 = SpriteAnimator(cwd + '/img/grass/grass03.jpg')
grass04 = SpriteAnimator(cwd + '/img/grass/grass04.jpg')
fireTorch = SpriteAnimator(cwd + '/img/character/elf/fire.jpg')
fireBall = SpriteAnimator(cwd + '/img/character/elf/fire2.jpg')
tree=SpriteAnimator(cwd + '/img/Trees/tree.png' )
tree_willow = SpriteAnimator(cwd + '/img/Trees/treeWillow.jpg')
stall_weapon = SpriteAnimator(cwd + '/img/Stall/weaponStall.jpg')

spriteDictionary = {"elf_demo": elf_demo, "orc": orc, "grass01": grass01, "grass02": grass02, "grass03": grass04,
                    'arrow': arrow,
                    "grass04": grass04, "fireBall": fireBall, "dog": dog,'whiteDragon':whiteDragon,'greenDragon':greenDragon,
                    "tree":tree, "water":water, "willow tree":tree_willow, "stall" = stall_weapon}

# -----------------------MOVING OBJECTS-------------------

# CAMERA
cam = Camera(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))

# PLAYER

player = Player(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y),
                Vector(PLAYER_INITIAL_VELOCITY_X, PLAYER_INITIAL_VELOCITY_Y), PLAYER_MAX_VELOCITY, PLAYER_INITIAL_ANGLE, PLAYER_RADIUS, PLAYER_SPRITE, spriteDictionary,PLAYER_SPRITE_FPS,
                PLAYER_ID)
player.setSpriteState(3)

player_list.append(player)

# MOUSE HANDLER (PYGAME)(NO RIGHT/MIDDLE CLICKS ON SIMPLEGUI)
mouse = Mouse()
# CONVERSION OF SIMPLE GUI MOUSE LOCATION TO PYGAME LOCATION
adjustment = Vector(250, 25)

# -----------------------NON-MOVING OBJECTS------------------

# GRASS
for x in range(20):
    for y in range(20):
        if (x == 0 or x == 19 or y == 0 or y == 19):
            tile_name = "water"
        else:
            tile_name = "grass01"
        
        g = Particle(False,Vector(x * 500, y * 500), Vector(0, 0),0,0,0,0,tile_name,spriteDictionary,0.0001,False,False)
        g.spriteSheet.setRow(1, 1, 1, 1, 1, 1)

        particle_set_bottom.add(g)

##dragon=Particle(True,Vector(0,2500),Vector(0,150),150,0,0,0,'whiteDragon',spriteDictionary,25,False,False)
##dragon.spriteSheet.setRow(5,4,1,1,5,4)
##dragon.move(Vector(10000,2500))
##moving_set.add(dragon)
##
##dragon2=Particle(True,Vector(0,2000),Vector(0,150),150,0,0,0,'greenDragon',spriteDictionary,25,False,False)
##dragon2.spriteSheet.setRow(5,4,1,1,5,4)
##dragon2.move(Vector(10000,2500))

tree_vector_list = []
while (len(tree_vector_list) < 100):
    x = random.randint(600, 9400)
    y = random.randint(600, 9400)
    v = Vector(x,y)

    valid = True
    for vector in tree_vector_list:
        if (v.distanceTo(vector) < 50):
            valid = False
            break

    if valid:
        tree_vector_list.append(v)

for vector in tree_vector_list:
    temp = Particle(False, vector, Vector(0, 0), 0, 0, 0, 0, "willow tree", spriteDictionary, 0.0001, False, False)
    temp.spriteSheet.setRow(1, 1, 1, 1, 1, 1)
    particle_set_middle.add(temp)

stall = Particle(False, Vector(500,500), Vector(0,0), 0, 0, 0, 0, "stall", spriteDictionary, 0.0001, False, False)
stall.spriteSheet.setRow(1, 1, 1, 1, 1, 1)
particle_set_middle.add(stall)

##tree=Particle(True,Vector(2500,2500),Vector(0,0),200,0,0,0,'tree',spriteDictionary,0.1,False,False)
##tree.spriteSheet.setRow(4,15,1,1,4,15)
