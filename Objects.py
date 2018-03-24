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
grass01 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
dog = SpriteAnimator(cwd + '/img/character/animals/dog.jpg')
grass02 = SpriteAnimator(cwd + '/img/grass/grass02.jpg')
grass03 = SpriteAnimator(cwd + '/img/grass/grass03.jpg')
grass04 = SpriteAnimator(cwd + '/img/grass/grass04.jpg')
fireTorch = SpriteAnimator(cwd + '/img/character/elf/fire.jpg')
fireBall = SpriteAnimator(cwd + '/img/character/elf/fire2.jpg', )
tree1 = SpriteAnimator(cwd + '/img/Trees/tree1.jpg')
tree2 = SpriteAnimator(cwd + '/img/Trees/tree2.jpg')
tree3 = SpriteAnimator(cwd + '/img/Trees/tree3.jpg')
tree4 = SpriteAnimator(cwd + '/img/Trees/tree4.jpg')
tree5 = SpriteAnimator(cwd + '/img/Trees/tree5.jpg')
tree6 = SpriteAnimator(cwd + '/img/Trees/tree6.jpg')
tree7 = SpriteAnimator(cwd + '/img/Trees/tree7.jpg')
tree8 = SpriteAnimator(cwd + '/img/Trees/tree8.jpg')

spriteDictionary = {"elf_demo": elf_demo, "orc": orc, "grass01": grass01, "grass02": grass02, "grass03": grass04,
                    'arrow': arrow,
                    "grass04": grass04, "fireBall": fireBall, "dog": dog,'whiteDragon':whiteDragon, "tree1": tree1,
                    "tree2": tree2, "tree3": tree3, "tree4": tree4,
                    "tree5": tree5, "tree6": tree6, "tree7": tree7, "tree8":tree8,}

# -----------------------MOVING OBJECTS-------------------

# CAMERA
cam = Camera(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))

# PLAYER

player = Player(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y),
                Vector(PLAYER_INITIAL_VELOCITY_X, PLAYER_INITIAL_VELOCITY_Y), PLAYER_MAX_VELOCITY, PLAYER_INITIAL_ANGLE,
                Vector(PLAYER_DIMENSIONS_X, PLAYER_DIMENSIONS_Y), PLAYER_RADIUS, PLAYER_SPRITE, spriteDictionary,PLAYER_SPRITE_FPS,
                PLAYER_ID)
player.setSpriteState(3)

player_list.append(player)

# MOUSE HANDLER (PYGAME)(NO RIGHT/MIDDLE CLICKS ON SIMPLEGUI)
mouse = Mouse()
# CONVERSION OF SIMPLE GUI MOUSE LOCATION TO PYGAME LOCATION
adjustment = Vector(250, 25)

# -----------------------NON-MOVING OBJECTS------------------

# GRASS
x = 0
for i in range(0, 400):
    if i % 20 == 0:
        x += 1
    g = Particle(Vector(x * 500, (i % 20) * 500), Vector(0, 0),0,0,0,0,'grass01',spriteDictionary,0.0001,False,False)

    g.spriteSheet.setRow(1, 1, 1, 1, 1, 1)

    particle_set_bottom.add(g)

dragon=Particle(Vector(2500,2500),Vector(0,100),200,0,0,0,'whiteDragon',spriteDictionary,20,False,False)
tree1=Particle(Vector(1300,1500), Vector(0,0),0,0,0,0,'tree1',spriteDictionary,5,False,False)
tree2=Particle(Vector(1000,4000), Vector(0,0),0,0,0,0,'tree2',spriteDictionary,5,False,False)
tree3=Particle(Vector(2300,5500), Vector(0,0),0,0,0,0,'tree3',spriteDictionary,5,False,False)
tree4=Particle(Vector(3500,3600), Vector(0,0),0,0,0,0,'tree4',spriteDictionary,5,False,False)
tree5=Particle(Vector(7300,7500), Vector(0,0),0,0,0,0,'tree5',spriteDictionary,5,False,False)
tree6=Particle(Vector(8300,5200), Vector(0,0),0,0,0,0,'tree6',spriteDictionary,5,False,False)
tree7=Particle(Vector(6700,4500), Vector(0,0),0,0,0,0,'tree7',spriteDictionary,5,False,False)
tree8=Particle(Vector(2300,1500), Vector(0,0),0,0,0,0,'tree8',spriteDictionary,5,False,False)

image = simpleguics2pygame.load_image(cwd+'/img/character/monsters/whiteDragon.jpg')
print(image.get_width())
dragon.move(Vector(10000,2500))
particle_set_top.add(dragon)
particle_set_top.add(tree1)
particle_set_top.add(tree2)
particle_set_top.add(tree3)
particle_set_top.add(tree4)
particle_set_top.add(tree5)
particle_set_top.add(tree6)
particle_set_top.add(tree7)
particle_set_top.add(tree8)


