from Classes.Settings import *
from Classes.Vector import Vector

from Classes.Camera import Camera
from Classes.Mouse import Mouse

from Classes.SpriteAnimator import SpriteAnimator
from Classes.Monster import Monster
from Classes.Player import Player
from Classes.Particle import Particle

from Classes.GameStates import GameState



import SimpleGUICS2Pygame
from SimpleGUICS2Pygame import simpleguics2pygame
import os
import random

#------------GAME STATES----------------
gameState1=GameState(True,False)
gameState2=GameState(True,False)

# ---------------------ANY SETS/LISTS-----------------------
moving_set = set()
particle_set_bottom = set()
particle_set_middle = set()
particle_set_top = set()
player_list = []
monster_set=set()
monster_set_external=set()

# MOUSE HANDLER (PYGAME)(NO RIGHT/MIDDLE CLICKS ON SIMPLEGUI)
mouse = Mouse()
# CONVERSION OF SIMPLE GUI MOUSE LOCATION TO PYGAME LOCATION
adjustment = Vector(250, 25)


def getUid():
    return str(uuid.uuid4())
# ------------------ DICTIONARY OF ALL PICTURES LOCATIONS-----------------

cwd = os.getcwd()

elf_demo = SpriteAnimator(cwd + '/img/character/elf/demo.jpg')
orc = SpriteAnimator(cwd + '/img/character/elf/orc.jpg')
arrow = SpriteAnimator(cwd + '/img/character/elf/arrow.jpg')
water = SpriteAnimator(cwd + '/img/Water/water.jpg')
dog = SpriteAnimator(cwd + '/img/character/animals/dog.jpg')
fireTorch = SpriteAnimator(cwd + '/img/character/elf/fire.jpg')
fireBall = SpriteAnimator(cwd + '/img/character/elf/fire2.jpg')
stall_weapon = SpriteAnimator(cwd + '/img/Stall/weaponStall.jpg')

monster_1_01 = SpriteAnimator(cwd + '/img/character/monsters/1/m1.jpg')
monster_1_02 = SpriteAnimator(cwd + '/img/character/monsters/1/m2.jpg')
monster_1_03 = SpriteAnimator(cwd + '/img/character/monsters/1/m3.jpg')

monster_2_01 = SpriteAnimator(cwd + '/img/character/monsters/2/m1.jpg')
monster_2_02 = SpriteAnimator(cwd + '/img/character/monsters/2/m2.jpg')

monster_3_01 = SpriteAnimator(cwd + '/img/character/monsters/3/m1.jpg')
monster_3_02 = SpriteAnimator(cwd + '/img/character/monsters/3/m2.jpg')
monster_3_03 = SpriteAnimator(cwd + '/img/character/monsters/3/m3.jpg')
monster_3_04 = SpriteAnimator(cwd + '/img/character/monsters/3/m4.jpg')

tree_01 = SpriteAnimator(cwd + '/img/trees/tree01.jpg')
tree_02 = SpriteAnimator(cwd + '/img/trees/tree02.jpg')
tree_03 = SpriteAnimator(cwd + '/img/trees/tree03.jpg')
tree_04 = SpriteAnimator(cwd + '/img/trees/tree04.jpg')

grass_01 = SpriteAnimator(cwd + '/img/grass/grass01.jpg')
grass_02 = SpriteAnimator(cwd + '/img/grass/grass02.jpg')
grass_03 = SpriteAnimator(cwd + '/img/grass/grass03.jpg')
grass_04 = SpriteAnimator(cwd + '/img/grass/grass04.jpg')
grass_05 = SpriteAnimator(cwd + '/img/grass/grass05.jpg')
grass_06 = SpriteAnimator(cwd + '/img/grass/grass06.jpg')
grass_07 = SpriteAnimator(cwd + '/img/grass/grass07.jpg')
grass_08 = SpriteAnimator(cwd + '/img/grass/grass08.jpg')
grass_09 = SpriteAnimator(cwd + '/img/grass/grass09.jpg')
grass_10 = SpriteAnimator(cwd + '/img/grass/grass10.jpg')
grass_11 = SpriteAnimator(cwd + '/img/grass/grass11.jpg')
grass_12 = SpriteAnimator(cwd + '/img/grass/grass12.jpg')
grass_13 = SpriteAnimator(cwd + '/img/grass/grass13.jpg')
grass_14 = SpriteAnimator(cwd + '/img/grass/grass14.jpg')
grass_15 = SpriteAnimator(cwd + '/img/grass/grass15.jpg')
grass_16 = SpriteAnimator(cwd + '/img/grass/grass16.jpg')
grass_17 = SpriteAnimator(cwd + '/img/grass/grass17.jpg')
grass_18 = SpriteAnimator(cwd + '/img/grass/grass18.jpg')
grass_19 = SpriteAnimator(cwd + '/img/grass/grass19.jpg')
grass_20 = SpriteAnimator(cwd + '/img/grass/grass20.jpg')
grass_21 = SpriteAnimator(cwd + '/img/grass/grass21.jpg')
grass_22 = SpriteAnimator(cwd + '/img/grass/grass22.jpg')

magic_01 = SpriteAnimator(cwd + '/img/Magic/magic (1).jpg')
magic_02 = SpriteAnimator(cwd + '/img/Magic/magic (2).jpg')
magic_03 = SpriteAnimator(cwd + '/img/Magic/magic (3).jpg')
magic_04 = SpriteAnimator(cwd + '/img/Magic/magic (4).jpg')
magic_05 = SpriteAnimator(cwd + '/img/Magic/magic (5).jpg')
magic_06 = SpriteAnimator(cwd + '/img/Magic/magic (6).jpg')
magic_07 = SpriteAnimator(cwd + '/img/Magic/magic (7).jpg')
magic_08 = SpriteAnimator(cwd + '/img/Magic/magic (8).jpg')
magic_09 = SpriteAnimator(cwd + '/img/Magic/magic (9).jpg')
magic_10 = SpriteAnimator(cwd + '/img/Magic/magic (10).jpg')
magic_11 = SpriteAnimator(cwd + '/img/Magic/magic (11).jpg')
magic_12 = SpriteAnimator(cwd + '/img/Magic/magic (12).jpg')
magic_13 = SpriteAnimator(cwd + '/img/Magic/magic (13).jpg')
magic_14 = SpriteAnimator(cwd + '/img/Magic/magic (14).jpg')
magic_15 = SpriteAnimator(cwd + '/img/Magic/magic (15).jpg')
magic_16 = SpriteAnimator(cwd + '/img/Magic/magic (16).jpg')
magic_17 = SpriteAnimator(cwd + '/img/Magic/magic (17).jpg')
magic_18 = SpriteAnimator(cwd + '/img/Magic/magic (18).jpg')
magic_19 = SpriteAnimator(cwd + '/img/Magic/magic (19).jpg')
magic_20 = SpriteAnimator(cwd + '/img/Magic/magic (20).jpg')
magic_21 = SpriteAnimator(cwd + '/img/Magic/magic (21).jpg')
magic_22 = SpriteAnimator(cwd + '/img/Magic/magic (22).jpg')
magic_23 = SpriteAnimator(cwd + '/img/Magic/magic (23).jpg')
magic_24 = SpriteAnimator(cwd + '/img/Magic/magic (24).jpg')
magic_25 = SpriteAnimator(cwd + '/img/Magic/magic (25).jpg')
magic_26 = SpriteAnimator(cwd + '/img/Magic/magic (26).jpg')
magic_27 = SpriteAnimator(cwd + '/img/Magic/magic (27).jpg')
magic_28 = SpriteAnimator(cwd + '/img/Magic/magic (28).jpg')
magic_29 = SpriteAnimator(cwd + '/img/Magic/magic (29).jpg')
magic_30 = SpriteAnimator(cwd + '/img/Magic/magic (30).jpg')
magic_31 = SpriteAnimator(cwd + '/img/Magic/magic (31).jpg')
magic_32 = SpriteAnimator(cwd + '/img/Magic/magic (32).jpg')
magic_33 = SpriteAnimator(cwd + '/img/Magic/magic (33).jpg')
magic_34 = SpriteAnimator(cwd + '/img/Magic/magic (34).jpg')
magic_35 = SpriteAnimator(cwd + '/img/Magic/magic (35).jpg')
magic_36 = SpriteAnimator(cwd + '/img/Magic/magic (36).jpg')
magic_37 = SpriteAnimator(cwd + '/img/Magic/magic (37).jpg')
magic_38 = SpriteAnimator(cwd + '/img/Magic/magic (38).jpg')
magic_39 = SpriteAnimator(cwd + '/img/Magic/magic (39).jpg')
magic_40 = SpriteAnimator(cwd + '/img/Magic/magic (40).jpg')
magic_41 = SpriteAnimator(cwd + '/img/Magic/magic (41).jpg')
magic_42 = SpriteAnimator(cwd + '/img/Magic/magic (42).jpg')
magic_43 = SpriteAnimator(cwd + '/img/Magic/magic (43).jpg')
magic_44 = SpriteAnimator(cwd + '/img/Magic/magic (44).jpg')
magic_45 = SpriteAnimator(cwd + '/img/Magic/magic (45).jpg')
magic_46 = SpriteAnimator(cwd + '/img/Magic/magic (46).jpg')
magic_47 = SpriteAnimator(cwd + '/img/Magic/magic (47).jpg')
magic_48 = SpriteAnimator(cwd + '/img/Magic/magic (48).jpg')
magic_49 = SpriteAnimator(cwd + '/img/Magic/magic (49).jpg')
magic_50 = SpriteAnimator(cwd + '/img/Magic/magic (50).jpg')
magic_51 = SpriteAnimator(cwd + '/img/Magic/magic (51).jpg')
magic_52 = SpriteAnimator(cwd + '/img/Magic/magic (52).jpg')
magic_53 = SpriteAnimator(cwd + '/img/Magic/magic (53).jpg')
magic_54 = SpriteAnimator(cwd + '/img/Magic/magic (54).jpg')
magic_55 = SpriteAnimator(cwd + '/img/Magic/magic (55).jpg')
magic_56 = SpriteAnimator(cwd + '/img/Magic/magic (56).jpg')
magic_57 = SpriteAnimator(cwd + '/img/Magic/magic (57).jpg')
magic_58 = SpriteAnimator(cwd + '/img/Magic/magic (58).jpg')
magic_59 = SpriteAnimator(cwd + '/img/Magic/magic (59).jpg')
magic_60 = SpriteAnimator(cwd + '/img/Magic/magic (60).jpg')
magic_61 = SpriteAnimator(cwd + '/img/Magic/magic (61).jpg')
magic_62 = SpriteAnimator(cwd + '/img/Magic/magic (62).jpg')
magic_63 = SpriteAnimator(cwd + '/img/Magic/magic (63).jpg')
magic_64 = SpriteAnimator(cwd + '/img/Magic/magic (64).jpg')
magic_65 = SpriteAnimator(cwd + '/img/Magic/magic (65).jpg')
magic_66 = SpriteAnimator(cwd + '/img/Magic/magic (66).jpg')
magic_67 = SpriteAnimator(cwd + '/img/Magic/magic (67).jpg')
magic_68 = SpriteAnimator(cwd + '/img/Magic/magic (68).jpg')
magic_69 = SpriteAnimator(cwd + '/img/Magic/magic (69).jpg')
magic_70 = SpriteAnimator(cwd + '/img/Magic/magic (70).jpg')
magic_71 = SpriteAnimator(cwd + '/img/Magic/magic (71).jpg')
magic_72 = SpriteAnimator(cwd + '/img/Magic/magic (72).jpg')
magic_73 = SpriteAnimator(cwd + '/img/Magic/magic (73).jpg')
magic_74 = SpriteAnimator(cwd + '/img/Magic/magic (74).jpg')
magic_75 = SpriteAnimator(cwd + '/img/Magic/magic (75).jpg')
magic_76 = SpriteAnimator(cwd + '/img/Magic/magic (76).jpg')
magic_77 = SpriteAnimator(cwd + '/img/Magic/magic (77).jpg')
magic_78 = SpriteAnimator(cwd + '/img/Magic/magic (78).jpg')
magic_79 = SpriteAnimator(cwd + '/img/Magic/magic (79).jpg')
magic_80 = SpriteAnimator(cwd + '/img/Magic/magic (80).jpg')
magic_81 = SpriteAnimator(cwd + '/img/Magic/magic (81).jpg')

spriteDictionary = {'elf_demo':elf_demo,
                    'orc':orc,
                    'arrow': arrow,
                    'fireBall': fireBall,
                    'dog':dog,
                    'whiteDragon':whiteDragon,
                    'greenDragon':greenDragon,
                    'water':water,
                    'stall' = stall_weapon,

                    'tree_01':tree_01,'tree_02':tree_02,
                    'tree_03':tree_03,'tree_04':tree_04,

                    'monster_1_01':monster_1_01,
                    'monster_1_02':monster_1_02,
                    'monster_1_03':monster_1_03,

                    'monster_2_01':monster_2_01,
                    'monster_2_02':monster_2_02,

                    'monster_3_01':monster_3_01,
                    'monster_3_02':monster_3_02,
                    'monster_3_03':monster_3_03,
                    'monster_3_04':monster_3_04,

                    'magic_01':magic_01,'magic_02':magic_02,'magic_03':magic_03,'magic_04':magic_04,
                    'magic_05':magic_05,'magic_06':magic_06,'magic_07':magic_07,'magic_08':magic_08,
                    'magic_09':magic_09,'magic_10':magic_10,'magic_11':magic_11,'magic_12':magic_12,
                    'magic_13':magic_13,'magic_14':magic_14,'magic_15':magic_15,'magic_16':magic_16,
                    'magic_17':magic_17,'magic_18':magic_18,'magic_19':magic_19,'magic_20':magic_20,
                    'magic_21':magic_21,'magic_22':magic_22,'magic_23':magic_23,'magic_24':magic_24,
                    'magic_25':magic_25,'magic_26':magic_26,'magic_27':magic_27,'magic_28':magic_28,
                    'magic_29':magic_29,'magic_30':magic_30,'magic_31':magic_31,'magic_32':magic_32,
                    'magic_33':magic_33,'magic_34':magic_34,'magic_35':magic_35,'magic_36':magic_36,
                    'magic_37':magic_37,'magic_38':magic_38,'magic_39':magic_39,'magic_40':magic_40,
                    'magic_41':magic_41,'magic_42':magic_42,'magic_43':magic_43,'magic_44':magic_44,
                    'magic_45':magic_45,'magic_46':magic_46,'magic_47':magic_47,'magic_48':magic_48,
                    'magic_49':magic_49,'magic_50':magic_50,'magic_51':magic_51,'magic_52':magic_52,
                    'magic_53':magic_53,'magic_54':magic_54,'magic_55':magic_55,'magic_56':magic_56,
                    'magic_57':magic_57,'magic_58':magic_58,'magic_59':magic_59,'magic_60':magic_60,
                    'magic_61':magic_61,'magic_62':magic_62,'magic_63':magic_63,'magic_64':magic_64,
                    'magic_65':magic_65,'magic_66':magic_66,'magic_67':magic_67,'magic_68':magic_68,
                    'magic_69':magic_69,'magic_70':magic_70,'magic_71':magic_71,'magic_72':magic_72,
                    'magic_73':magic_73,'magic_74':magic_74,'magic_75':magic_75,'magic_76':magic_76,
                    'magic_77':magic_77,'magic_78':magic_78,'magic_79':magic_79,'magic_80':magic_80,
                    'magic_81':magic_81,

                    'grass_01':grass_01,'grass_02':grass_02,'grass_03':grass_03,'grass_04':grass_04,
                    'grass_05':grass_05,'grass_06':grass_06,'grass_07':grass_07,'grass_08':grass_08,
                    'grass_09':grass_09,'grass_10':grass_10,'grass_11':grass_11,'grass_12':grass_12,
                    'grass_13':grass_13,'grass_14':grass_14,'grass_15':grass_15,'grass_16':grass_16,
                    'grass_17':grass_17,'grass_18':grass_18,'grass_19':grass_19,'grass_20':grass_20,
                    'grass_21':grass_21,'grass_22':grass_22
                    }

# -----------------------MOVING OBJECTS-------------------

# CAMERA
cam = Camera(Vector(PLAYER_INITIAL_POSITION_X, PLAYER_INITIAL_POSITION_Y), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))

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



if (bool(config['NETWORKING']['CONFIG_TYPE'] == "server")):
    dragon = Monster(Vector(0, 2500), Vector(100, 0), 0, Vector(0, 2500), 150, 0, 0, 'whiteDragon', spriteDictionary,
                     25, getUid(), False, Vector(0, 0), 1, 5, 4, 1, 1, 5, 4)
    dragon.move(Vector(10000, 2500))
    monster_set.add(dragon)

elif bool((config['NETWORKING']['CONFIG_TYPE'] == "client")):
    dragon2=Monster(Vector(0,3000),Vector(100,0),0,Vector(0,3000),150,0,0,'greenDragon',spriteDictionary,25,getUid(),False,Vector(0,0),1,5,4,1,1,5,4)
    dragon2.move(Vector(10000,2500))
    monster_set.add(dragon2)








# -----------------------NON-MOVING OBJECTS------------------

# GRASS
x = 0

for i in range(0, 400):
    if i % 20 == 0:
        x += 1
   
    g = Particle(False,Vector(x * 500, (i % 20) * 500), Vector(0, 0),0,Vector(x * 500, (i % 20) * 500),0,0,0,0,'grass01',spriteDictionary,0.0001,False,False,getUid(),1, 1, 1, 1, 1, 1)

    particle_set_bottom.add(g)

tree=Particle(True,Vector(2500,2500),Vector(0,0),0,Vector(2500,2500),200,0,0,0,'tree',spriteDictionary,1,False,False,getUid(),4,15,1,1,4,15)


tree=Particle(True,Vector(2500,2500),Vector(0,0),200,0,0,0,'tree',spriteDictionary,0.1,False,False)
tree.spriteSheet.setRow(4,15,1,1,4,15)
