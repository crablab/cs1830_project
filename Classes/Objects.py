from Classes.Settings import *
import configparser, json, uuid, os, random
config = configparser.ConfigParser()
config.read_file(open('Classes/config'))
from Classes.Vector import Vector

from Classes.Camera import Camera
from Classes.Mouse import Mouse

from Classes.SpriteAnimator import SpriteAnimator
from Classes.Monster import Monster
from Classes.Player import Player
from Classes.Particle import Particle


import SimpleGUICS2Pygame
from SimpleGUICS2Pygame import simpleguics2pygame


# ---------------------ANY SETS/LISTS-----------------------
moving_set = set()
moving_set_external=set()
particle_set_bottom = set()
particle_set_middle = set()
particle_set_top = set()
player_list = []
monster_set=set()
monster_set_external=set()


def getUid():
    return str(uuid.uuid4())
# ------------------ DICTIONARY OF ALL PICTURES LOCATIONS-----------------

cwd = os.getcwd()
elf_demo = SpriteAnimator(cwd + '/img/character/elf/demo.jpg')
orc = SpriteAnimator(cwd + '/img/character/elf/orc.jpg')
arrow = SpriteAnimator(cwd + '/img/character/elf/arrow.jpg')
whiteDragon=SpriteAnimator(cwd+'/img/character/monsters/whiteDragon.jpg')
greenDragon=SpriteAnimator(cwd+'/img/character/monsters/greenDragon.jpg')
grass01 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
dog = SpriteAnimator(cwd + '/img/character/animals/dog.jpg')
grass02 = SpriteAnimator(cwd + '/img/grass/grass02.jpg')
grass03 = SpriteAnimator(cwd + '/img/grass/grass03.jpg')
grass04 = SpriteAnimator(cwd + '/img/grass/grass04.jpg')
fireTorch = SpriteAnimator(cwd + '/img/character/elf/fire.jpg')
fireBall = SpriteAnimator(cwd + '/img/character/elf/fire2.jpg')
tree=SpriteAnimator(cwd + '/img/trees/tree.png' )

spriteDictionary = {"elf_demo": elf_demo, "orc": orc, "grass01": grass01, "grass02": grass02, "grass03": grass04,
                    'arrow': arrow,
                    "grass04": grass04, "fireBall": fireBall, "dog": dog,'whiteDragon':whiteDragon,'greenDragon':greenDragon,
                    "tree":tree}

# -----------------------MOVING OBJECTS-------------------
print(int(config['PLAYER']['PLAYER_INITIAL_POSITION_X']))
print(int(config['PLAYER']['PLAYER_INITIAL_POSITION_Y']))
print(int(config['CANVAS']['CANVAS_WIDTH']))
print(int(config['CANVAS']['CANVAS_HEIGHT']))
print(config['PLAYER']['PLAYER_SPRITE'])
# CAMERA
cam = Camera(Vector(int(config['PLAYER']['PLAYER_INITIAL_POSITION_X']), int(config['PLAYER']['PLAYER_INITIAL_POSITION_Y'])), Vector(int(config['CANVAS']['CANVAS_WIDTH']), int(config['CANVAS']['CANVAS_HEIGHT'])))
print(cam.origin)
print(cam.dim)
# PLAYER

player1 = Player(Vector(int(config['PLAYER']['PLAYER_INITIAL_POSITION_X']), int(config['PLAYER']['PLAYER_INITIAL_POSITION_Y'])),
                Vector(int(config['PLAYER']['PLAYER_INITIAL_VELOCITY_X']),int(config['PLAYER']['PLAYER_INITIAL_VELOCITY_Y'])),
                 0,Vector(int(config['PLAYER']['PLAYER_INITIAL_POSITION_X']), int(config['PLAYER']['PLAYER_INITIAL_POSITION_Y'])),
                 int(config['PLAYER']['PLAYER_MAX_VELOCITY']),
                 int(config['PLAYER']['PLAYER_INITIAL_ANGLE']),
                 int(config['PLAYER']['PLAYER_RADIUS']),
                 config['PLAYER']['PLAYER_SPRITE'],
                 spriteDictionary,
                 int(config['PLAYER']['PLAYER_SPRITE_FPS']),
                str(getUid()),

                 False,Vector(0,0),1,21, 13, 11, 1, 9, 9)
player1.setSpriteState(3)
player_list.append(player1)
playerId=player1.idObject

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

    g = Particle(False,Vector(x * 500, (i % 20) * 500), Vector(0, 0),0,Vector(x * 500, (i % 20) * 500),0,0,0,0,'grass01',spriteDictionary,0.0001,False,False,getUid(),1, 1, 1, 1, 1, 1)

    particle_set_bottom.add(g)

dragon=Monster(Vector(0,2500),Vector(100,0),0,Vector(0,2500),150,0,0,'whiteDragon',spriteDictionary,25,getUid(),False,Vector(0,0),1,5,4,1,1,5,4)
dragon.move(Vector(10000,2500))
monster_set.add(dragon)

dragon2=Monster(Vector(0,3000),Vector(100,0),0,Vector(0,3000),150,0,0,'greenDragon',spriteDictionary,25,getUid(),False,Vector(0,0),1,5,4,1,1,5,4)
dragon2.move(Vector(10000,2500))
monster_set.add(dragon2)

tree=Particle(True,Vector(2500,2500),Vector(0,0),0,Vector(2500,2500),200,0,0,0,'tree',spriteDictionary,1,False,False,getUid(),4,15,1,1,4,15)
Particle()
particle_set_middle.add(tree)
