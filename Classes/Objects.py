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

tree_01 = SpriteAnimator(cwd + '/img/grass/tree01.jpg')
tree_02 = SpriteAnimator(cwd + '/img/grass/tree02.jpg')
tree_03 = SpriteAnimator(cwd + '/img/grass/tree03.jpg')
tree_04 = SpriteAnimator(cwd + '/img/grass/tree04.jpg')
tree_05 = SpriteAnimator(cwd + '/img/grass/tree05.jpg')
tree_06 = SpriteAnimator(cwd + '/img/grass/tree06.jpg')
tree_07 = SpriteAnimator(cwd + '/img/grass/tree07.jpg')
tree_08 = SpriteAnimator(cwd + '/img/grass/tree08.jpg')
tree_09 = SpriteAnimator(cwd + '/img/grass/tree09.jpg')
tree_10 = SpriteAnimator(cwd + '/img/grass/tree10.jpg')
tree_11 = SpriteAnimator(cwd + '/img/grass/tree11.jpg')
tree_12 = SpriteAnimator(cwd + '/img/grass/tree12.jpg')

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

animal_000 = SpriteAnimator(cwd + '/img/character/animals/3x4/000.jpg')
animal_001 = SpriteAnimator(cwd + '/img/character/animals/3x4/001.jpg')
animal_002 = SpriteAnimator(cwd + '/img/character/animals/3x4/002.jpg')
animal_003 = SpriteAnimator(cwd + '/img/character/animals/3x4/003.jpg')
animal_004 = SpriteAnimator(cwd + '/img/character/animals/3x4/004.jpg')
animal_005 = SpriteAnimator(cwd + '/img/character/animals/3x4/005.jpg')
animal_006 = SpriteAnimator(cwd + '/img/character/animals/3x4/006.jpg')
animal_007 = SpriteAnimator(cwd + '/img/character/animals/3x4/007.jpg')
animal_008 = SpriteAnimator(cwd + '/img/character/animals/3x4/008.jpg')
animal_009 = SpriteAnimator(cwd + '/img/character/animals/3x4/009.jpg')
animal_010 = SpriteAnimator(cwd + '/img/character/animals/3x4/010.jpg')
animal_011 = SpriteAnimator(cwd + '/img/character/animals/3x4/011.jpg')
animal_012 = SpriteAnimator(cwd + '/img/character/animals/3x4/012.jpg')
animal_013 = SpriteAnimator(cwd + '/img/character/animals/3x4/013.jpg')
animal_014 = SpriteAnimator(cwd + '/img/character/animals/3x4/014.jpg')
animal_015 = SpriteAnimator(cwd + '/img/character/animals/3x4/015.jpg')
animal_016 = SpriteAnimator(cwd + '/img/character/animals/3x4/016.jpg')
animal_017 = SpriteAnimator(cwd + '/img/character/animals/3x4/017.jpg')
animal_018 = SpriteAnimator(cwd + '/img/character/animals/3x4/018.jpg')
animal_019 = SpriteAnimator(cwd + '/img/character/animals/3x4/019.jpg')
animal_020 = SpriteAnimator(cwd + '/img/character/animals/3x4/020.jpg')
animal_021 = SpriteAnimator(cwd + '/img/character/animals/3x4/021.jpg')
animal_022 = SpriteAnimator(cwd + '/img/character/animals/3x4/022.jpg')
animal_023 = SpriteAnimator(cwd + '/img/character/animals/3x4/023.jpg')
animal_024 = SpriteAnimator(cwd + '/img/character/animals/3x4/024.jpg')
animal_025 = SpriteAnimator(cwd + '/img/character/animals/3x4/025.jpg')
animal_026 = SpriteAnimator(cwd + '/img/character/animals/3x4/026.jpg')
animal_027 = SpriteAnimator(cwd + '/img/character/animals/3x4/027.jpg')
animal_028 = SpriteAnimator(cwd + '/img/character/animals/3x4/028.jpg')
animal_029 = SpriteAnimator(cwd + '/img/character/animals/3x4/029.jpg')
animal_030 = SpriteAnimator(cwd + '/img/character/animals/3x4/030.jpg')
animal_031 = SpriteAnimator(cwd + '/img/character/animals/3x4/031.jpg')
animal_032 = SpriteAnimator(cwd + '/img/character/animals/3x4/032.jpg')
animal_033 = SpriteAnimator(cwd + '/img/character/animals/3x4/033.jpg')
animal_034 = SpriteAnimator(cwd + '/img/character/animals/3x4/034.jpg')
animal_035 = SpriteAnimator(cwd + '/img/character/animals/3x4/035.jpg')
animal_036 = SpriteAnimator(cwd + '/img/character/animals/3x4/036.jpg')
animal_037 = SpriteAnimator(cwd + '/img/character/animals/3x4/037.jpg')
animal_038 = SpriteAnimator(cwd + '/img/character/animals/3x4/038.jpg')
animal_039 = SpriteAnimator(cwd + '/img/character/animals/3x4/039.jpg')
animal_040 = SpriteAnimator(cwd + '/img/character/animals/3x4/040.jpg')
animal_041 = SpriteAnimator(cwd + '/img/character/animals/3x4/041.jpg')
animal_042 = SpriteAnimator(cwd + '/img/character/animals/3x4/042.jpg')
animal_043 = SpriteAnimator(cwd + '/img/character/animals/3x4/043.jpg')
animal_044 = SpriteAnimator(cwd + '/img/character/animals/3x4/044.jpg')
animal_045 = SpriteAnimator(cwd + '/img/character/animals/3x4/045.jpg')
animal_046 = SpriteAnimator(cwd + '/img/character/animals/3x4/046.jpg')
animal_047 = SpriteAnimator(cwd + '/img/character/animals/3x4/047.jpg')
animal_048 = SpriteAnimator(cwd + '/img/character/animals/3x4/048.jpg')
animal_049 = SpriteAnimator(cwd + '/img/character/animals/3x4/049.jpg')
animal_050 = SpriteAnimator(cwd + '/img/character/animals/3x4/050.jpg')
animal_051 = SpriteAnimator(cwd + '/img/character/animals/3x4/051.jpg')
animal_052 = SpriteAnimator(cwd + '/img/character/animals/3x4/052.jpg')
animal_053 = SpriteAnimator(cwd + '/img/character/animals/3x4/053.jpg')
animal_054 = SpriteAnimator(cwd + '/img/character/animals/3x4/054.jpg')
animal_055 = SpriteAnimator(cwd + '/img/character/animals/3x4/055.jpg')
animal_056 = SpriteAnimator(cwd + '/img/character/animals/3x4/056.jpg')
animal_057 = SpriteAnimator(cwd + '/img/character/animals/3x4/057.jpg')
animal_058 = SpriteAnimator(cwd + '/img/character/animals/3x4/058.jpg')
animal_059 = SpriteAnimator(cwd + '/img/character/animals/3x4/059.jpg')
animal_060 = SpriteAnimator(cwd + '/img/character/animals/3x4/060.jpg')
animal_061 = SpriteAnimator(cwd + '/img/character/animals/3x4/061.jpg')
animal_062 = SpriteAnimator(cwd + '/img/character/animals/3x4/062.jpg')
animal_063 = SpriteAnimator(cwd + '/img/character/animals/3x4/063.jpg')
animal_064 = SpriteAnimator(cwd + '/img/character/animals/3x4/064.jpg')
animal_065 = SpriteAnimator(cwd + '/img/character/animals/3x4/065.jpg')
animal_066 = SpriteAnimator(cwd + '/img/character/animals/3x4/066.jpg')
animal_067 = SpriteAnimator(cwd + '/img/character/animals/3x4/067.jpg')
animal_068 = SpriteAnimator(cwd + '/img/character/animals/3x4/068.jpg')
animal_069 = SpriteAnimator(cwd + '/img/character/animals/3x4/069.jpg')
animal_070 = SpriteAnimator(cwd + '/img/character/animals/3x4/070.jpg')
animal_071 = SpriteAnimator(cwd + '/img/character/animals/3x4/071.jpg')
animal_072 = SpriteAnimator(cwd + '/img/character/animals/3x4/072.jpg')
animal_073 = SpriteAnimator(cwd + '/img/character/animals/3x4/073.jpg')
animal_074 = SpriteAnimator(cwd + '/img/character/animals/3x4/074.jpg')
animal_075 = SpriteAnimator(cwd + '/img/character/animals/3x4/075.jpg')
animal_076 = SpriteAnimator(cwd + '/img/character/animals/3x4/076.jpg')
animal_077 = SpriteAnimator(cwd + '/img/character/animals/3x4/077.jpg')
animal_078 = SpriteAnimator(cwd + '/img/character/animals/3x4/078.jpg')
animal_079 = SpriteAnimator(cwd + '/img/character/animals/3x4/079.jpg')
animal_080 = SpriteAnimator(cwd + '/img/character/animals/3x4/080.jpg')
animal_081 = SpriteAnimator(cwd + '/img/character/animals/3x4/081.jpg')
animal_082 = SpriteAnimator(cwd + '/img/character/animals/3x4/082.jpg')
animal_083 = SpriteAnimator(cwd + '/img/character/animals/3x4/083.jpg')
animal_084 = SpriteAnimator(cwd + '/img/character/animals/3x4/084.jpg')
animal_085 = SpriteAnimator(cwd + '/img/character/animals/3x4/085.jpg')
animal_086 = SpriteAnimator(cwd + '/img/character/animals/3x4/086.jpg')
animal_087 = SpriteAnimator(cwd + '/img/character/animals/3x4/087.jpg')
animal_088 = SpriteAnimator(cwd + '/img/character/animals/3x4/088.jpg')
animal_089 = SpriteAnimator(cwd + '/img/character/animals/3x4/089.jpg')
animal_090 = SpriteAnimator(cwd + '/img/character/animals/3x4/090.jpg')
animal_091 = SpriteAnimator(cwd + '/img/character/animals/3x4/091.jpg')
animal_092 = SpriteAnimator(cwd + '/img/character/animals/3x4/092.jpg')
animal_093 = SpriteAnimator(cwd + '/img/character/animals/3x4/093.jpg')
animal_094 = SpriteAnimator(cwd + '/img/character/animals/3x4/094.jpg')
animal_095 = SpriteAnimator(cwd + '/img/character/animals/3x4/095.jpg')
animal_096 = SpriteAnimator(cwd + '/img/character/animals/3x4/096.jpg')
animal_097 = SpriteAnimator(cwd + '/img/character/animals/3x4/097.jpg')
animal_098 = SpriteAnimator(cwd + '/img/character/animals/3x4/098.jpg')
animal_099 = SpriteAnimator(cwd + '/img/character/animals/3x4/099.jpg')
animal_100 = SpriteAnimator(cwd + '/img/character/animals/3x4/100.jpg')
animal_101 = SpriteAnimator(cwd + '/img/character/animals/3x4/101.jpg')
animal_102 = SpriteAnimator(cwd + '/img/character/animals/3x4/102.jpg')
animal_103 = SpriteAnimator(cwd + '/img/character/animals/3x4/103.jpg')
animal_104 = SpriteAnimator(cwd + '/img/character/animals/3x4/104.jpg')
animal_105 = SpriteAnimator(cwd + '/img/character/animals/3x4/105.jpg')
animal_106 = SpriteAnimator(cwd + '/img/character/animals/3x4/106.jpg')
animal_107 = SpriteAnimator(cwd + '/img/character/animals/3x4/107.jpg')
animal_108 = SpriteAnimator(cwd + '/img/character/animals/3x4/108.jpg')
animal_109 = SpriteAnimator(cwd + '/img/character/animals/3x4/109.jpg')
animal_110 = SpriteAnimator(cwd + '/img/character/animals/3x4/110.jpg')
animal_111 = SpriteAnimator(cwd + '/img/character/animals/3x4/111.jpg')
animal_112 = SpriteAnimator(cwd + '/img/character/animals/3x4/112.jpg')
animal_113 = SpriteAnimator(cwd + '/img/character/animals/3x4/113.jpg')
animal_114 = SpriteAnimator(cwd + '/img/character/animals/3x4/114.jpg')
animal_115 = SpriteAnimator(cwd + '/img/character/animals/3x4/115.jpg')
animal_116 = SpriteAnimator(cwd + '/img/character/animals/3x4/116.jpg')
animal_117 = SpriteAnimator(cwd + '/img/character/animals/3x4/117.jpg')
animal_118 = SpriteAnimator(cwd + '/img/character/animals/3x4/118.jpg')
animal_119 = SpriteAnimator(cwd + '/img/character/animals/3x4/119.jpg')
animal_120 = SpriteAnimator(cwd + '/img/character/animals/3x4/120.jpg')
animal_121 = SpriteAnimator(cwd + '/img/character/animals/3x4/121.jpg')
animal_122 = SpriteAnimator(cwd + '/img/character/animals/3x4/122.jpg')
animal_123 = SpriteAnimator(cwd + '/img/character/animals/3x4/123.jpg')
animal_124 = SpriteAnimator(cwd + '/img/character/animals/3x4/124.jpg')
animal_125 = SpriteAnimator(cwd + '/img/character/animals/3x4/125.jpg')
animal_126 = SpriteAnimator(cwd + '/img/character/animals/3x4/126.jpg')
animal_127 = SpriteAnimator(cwd + '/img/character/animals/3x4/127.jpg')
animal_128 = SpriteAnimator(cwd + '/img/character/animals/3x4/128.jpg')
animal_129 = SpriteAnimator(cwd + '/img/character/animals/3x4/129.jpg')
animal_130 = SpriteAnimator(cwd + '/img/character/animals/3x4/130.jpg')
animal_131 = SpriteAnimator(cwd + '/img/character/animals/3x4/131.jpg')
animal_132 = SpriteAnimator(cwd + '/img/character/animals/3x4/132.jpg')
animal_133 = SpriteAnimator(cwd + '/img/character/animals/3x4/133.jpg')
animal_134 = SpriteAnimator(cwd + '/img/character/animals/3x4/134.jpg')
animal_135 = SpriteAnimator(cwd + '/img/character/animals/3x4/135.jpg')
animal_136 = SpriteAnimator(cwd + '/img/character/animals/3x4/136.jpg')
animal_137 = SpriteAnimator(cwd + '/img/character/animals/3x4/137.jpg')
animal_138 = SpriteAnimator(cwd + '/img/character/animals/3x4/138.jpg')
animal_139 = SpriteAnimator(cwd + '/img/character/animals/3x4/139.jpg')
animal_140 = SpriteAnimator(cwd + '/img/character/animals/3x4/140.jpg')
animal_141 = SpriteAnimator(cwd + '/img/character/animals/3x4/141.jpg')
animal_142 = SpriteAnimator(cwd + '/img/character/animals/3x4/142.jpg')
animal_143 = SpriteAnimator(cwd + '/img/character/animals/3x4/143.jpg')
animal_144 = SpriteAnimator(cwd + '/img/character/animals/3x4/144.jpg')
animal_145 = SpriteAnimator(cwd + '/img/character/animals/3x4/145.jpg')
animal_146 = SpriteAnimator(cwd + '/img/character/animals/3x4/146.jpg')
animal_147 = SpriteAnimator(cwd + '/img/character/animals/3x4/147.jpg')
animal_148 = SpriteAnimator(cwd + '/img/character/animals/3x4/148.jpg')
animal_149 = SpriteAnimator(cwd + '/img/character/animals/3x4/149.jpg')
animal_150 = SpriteAnimator(cwd + '/img/character/animals/3x4/150.jpg')
animal_151 = SpriteAnimator(cwd + '/img/character/animals/3x4/151.jpg')
animal_152 = SpriteAnimator(cwd + '/img/character/animals/3x4/152.jpg')
animal_153 = SpriteAnimator(cwd + '/img/character/animals/3x4/153.jpg')
animal_154 = SpriteAnimator(cwd + '/img/character/animals/3x4/154.jpg')
animal_155 = SpriteAnimator(cwd + '/img/character/animals/3x4/155.jpg')
animal_156 = SpriteAnimator(cwd + '/img/character/animals/3x4/156.jpg')
animal_157 = SpriteAnimator(cwd + '/img/character/animals/3x4/157.jpg')
animal_158 = SpriteAnimator(cwd + '/img/character/animals/3x4/158.jpg')
animal_159 = SpriteAnimator(cwd + '/img/character/animals/3x4/159.jpg')
animal_160 = SpriteAnimator(cwd + '/img/character/animals/3x4/160.jpg')
animal_161 = SpriteAnimator(cwd + '/img/character/animals/3x4/161.jpg')
animal_162 = SpriteAnimator(cwd + '/img/character/animals/3x4/162.jpg')
animal_163 = SpriteAnimator(cwd + '/img/character/animals/3x4/163.jpg')
animal_164 = SpriteAnimator(cwd + '/img/character/animals/3x4/164.jpg')
animal_165 = SpriteAnimator(cwd + '/img/character/animals/3x4/165.jpg')
animal_166 = SpriteAnimator(cwd + '/img/character/animals/3x4/166.jpg')
animal_167 = SpriteAnimator(cwd + '/img/character/animals/3x4/167.jpg')
animal_168 = SpriteAnimator(cwd + '/img/character/animals/3x4/168.jpg')
animal_169 = SpriteAnimator(cwd + '/img/character/animals/3x4/169.jpg')
animal_170 = SpriteAnimator(cwd + '/img/character/animals/3x4/170.jpg')
animal_171 = SpriteAnimator(cwd + '/img/character/animals/3x4/171.jpg')
animal_172 = SpriteAnimator(cwd + '/img/character/animals/3x4/172.jpg')
animal_173 = SpriteAnimator(cwd + '/img/character/animals/3x4/173.jpg')
animal_174 = SpriteAnimator(cwd + '/img/character/animals/3x4/174.jpg')
animal_175 = SpriteAnimator(cwd + '/img/character/animals/3x4/175.jpg')
animal_176 = SpriteAnimator(cwd + '/img/character/animals/3x4/176.jpg')
animal_177 = SpriteAnimator(cwd + '/img/character/animals/3x4/177.jpg')
animal_178 = SpriteAnimator(cwd + '/img/character/animals/3x4/178.jpg')
animal_179 = SpriteAnimator(cwd + '/img/character/animals/3x4/179.jpg')
animal_180 = SpriteAnimator(cwd + '/img/character/animals/3x4/180.jpg')
animal_181 = SpriteAnimator(cwd + '/img/character/animals/3x4/181.jpg')
animal_182 = SpriteAnimator(cwd + '/img/character/animals/3x4/182.jpg')
animal_183 = SpriteAnimator(cwd + '/img/character/animals/3x4/183.jpg')
animal_184 = SpriteAnimator(cwd + '/img/character/animals/3x4/184.jpg')
animal_185 = SpriteAnimator(cwd + '/img/character/animals/3x4/185.jpg')
animal_186 = SpriteAnimator(cwd + '/img/character/animals/3x4/186.jpg')
animal_187 = SpriteAnimator(cwd + '/img/character/animals/3x4/187.jpg')
animal_188 = SpriteAnimator(cwd + '/img/character/animals/3x4/188.jpg')
animal_189 = SpriteAnimator(cwd + '/img/character/animals/3x4/189.jpg')
animal_190 = SpriteAnimator(cwd + '/img/character/animals/3x4/190.jpg')
animal_191 = SpriteAnimator(cwd + '/img/character/animals/3x4/191.jpg')
animal_192 = SpriteAnimator(cwd + '/img/character/animals/3x4/192.jpg')
animal_193 = SpriteAnimator(cwd + '/img/character/animals/3x4/193.jpg')
animal_194 = SpriteAnimator(cwd + '/img/character/animals/3x4/194.jpg')
animal_195 = SpriteAnimator(cwd + '/img/character/animals/3x4/195.jpg')
animal_196 = SpriteAnimator(cwd + '/img/character/animals/3x4/196.jpg')
animal_197 = SpriteAnimator(cwd + '/img/character/animals/3x4/197.jpg')
animal_198 = SpriteAnimator(cwd + '/img/character/animals/3x4/198.jpg')
animal_199 = SpriteAnimator(cwd + '/img/character/animals/3x4/199.jpg')
animal_200 = SpriteAnimator(cwd + '/img/character/animals/3x4/200.jpg')
animal_201 = SpriteAnimator(cwd + '/img/character/animals/3x4/201.jpg')
animal_202 = SpriteAnimator(cwd + '/img/character/animals/3x4/202.jpg')
animal_203 = SpriteAnimator(cwd + '/img/character/animals/3x4/203.jpg')
animal_204 = SpriteAnimator(cwd + '/img/character/animals/3x4/204.jpg')
animal_205 = SpriteAnimator(cwd + '/img/character/animals/3x4/205.jpg')
animal_206 = SpriteAnimator(cwd + '/img/character/animals/3x4/206.jpg')
animal_207 = SpriteAnimator(cwd + '/img/character/animals/3x4/207.jpg')
animal_208 = SpriteAnimator(cwd + '/img/character/animals/3x4/208.jpg')
animal_209 = SpriteAnimator(cwd + '/img/character/animals/3x4/209.jpg')
animal_210 = SpriteAnimator(cwd + '/img/character/animals/3x4/210.jpg')
animal_211 = SpriteAnimator(cwd + '/img/character/animals/3x4/211.jpg')
animal_212 = SpriteAnimator(cwd + '/img/character/animals/3x4/212.jpg')
animal_213 = SpriteAnimator(cwd + '/img/character/animals/3x4/213.jpg')
animal_214 = SpriteAnimator(cwd + '/img/character/animals/3x4/214.jpg')
animal_215 = SpriteAnimator(cwd + '/img/character/animals/3x4/215.jpg')
animal_216 = SpriteAnimator(cwd + '/img/character/animals/3x4/216.jpg')
animal_217 = SpriteAnimator(cwd + '/img/character/animals/3x4/217.jpg')

spriteDictionary = {'elf_demo':elf_demo,
                    'orc':orc,
                    'arrow': arrow,
                    'fireBall': fireBall,
                    'dog':dog,
                    'whiteDragon':whiteDragon,
                    'greenDragon':greenDragon,
                    'water':water,
                    'stall' = stall_weapon,

                    'tree_01':tree_01,'tree_02':tree_02,'tree_03':tree_03,'tree_04':tree_04,
                    'tree_05':tree_05,'tree_06':tree_06,'tree_07':tree_07,'tree_08':tree_08,
                    'tree_09':tree_09,'tree_10':tree_10,'tree_11':tree_11,'tree_12':tree_12,

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
                    'grass_21':grass_21,'grass_22':grass_22,

                    'animal_000':animal_000,'animal_001':animal_001,'animal_002':animal_002,'animal_003':animal_003,
                    'animal_004':animal_004,'animal_005':animal_005,'animal_006':animal_006,'animal_007':animal_007,
                    'animal_008':animal_008,'animal_009':animal_009,'animal_010':animal_010,'animal_011':animal_011,
                    'animal_012':animal_012,'animal_013':animal_013,'animal_014':animal_014,'animal_015':animal_015,
                    'animal_016':animal_016,'animal_017':animal_017,'animal_018':animal_018,'animal_019':animal_019,
                    'animal_020':animal_020,'animal_021':animal_021,'animal_022':animal_022,'animal_023':animal_023,
                    'animal_024':animal_024,'animal_025':animal_025,'animal_026':animal_026,'animal_027':animal_027,
                    'animal_028':animal_028,'animal_029':animal_029,'animal_030':animal_030,'animal_031':animal_031,
                    'animal_032':animal_032,'animal_033':animal_033,'animal_034':animal_034,'animal_035':animal_035,
                    'animal_036':animal_036,'animal_037':animal_037,'animal_038':animal_038,'animal_039':animal_039,
                    'animal_040':animal_040,'animal_041':animal_041,'animal_042':animal_042,'animal_043':animal_043,
                    'animal_044':animal_044,'animal_045':animal_045,'animal_046':animal_046,'animal_047':animal_047,
                    'animal_048':animal_048,'animal_049':animal_049,'animal_050':animal_050,'animal_051':animal_051,
                    'animal_052':animal_052,'animal_053':animal_053,'animal_054':animal_054,'animal_055':animal_055,
                    'animal_056':animal_056,'animal_057':animal_057,'animal_058':animal_058,'animal_059':animal_059,
                    'animal_060':animal_060,'animal_061':animal_061,'animal_062':animal_062,'animal_063':animal_063,
                    'animal_064':animal_064,'animal_065':animal_065,'animal_066':animal_066,'animal_067':animal_067,
                    'animal_068':animal_068,'animal_069':animal_069,'animal_070':animal_070,'animal_071':animal_071,
                    'animal_072':animal_072,'animal_073':animal_073,'animal_074':animal_074,'animal_075':animal_075,
                    'animal_076':animal_076,'animal_077':animal_077,'animal_078':animal_078,'animal_079':animal_079,
                    'animal_080':animal_080,'animal_081':animal_081,'animal_082':animal_082,'animal_083':animal_083,
                    'animal_084':animal_084,'animal_085':animal_085,'animal_086':animal_086,'animal_087':animal_087,
                    'animal_088':animal_088,'animal_089':animal_089,'animal_090':animal_090,'animal_091':animal_091,
                    'animal_092':animal_092,'animal_093':animal_093,'animal_094':animal_094,'animal_095':animal_095,
                    'animal_096':animal_096,'animal_097':animal_097,'animal_098':animal_098,'animal_099':animal_099,
                    'animal_100':animal_100,'animal_101':animal_101,'animal_102':animal_102,'animal_103':animal_103,
                    'animal_104':animal_104,'animal_105':animal_105,'animal_106':animal_106,'animal_107':animal_107,
                    'animal_108':animal_108,'animal_109':animal_109,'animal_110':animal_110,'animal_111':animal_111,
                    'animal_112':animal_112,'animal_113':animal_113,'animal_114':animal_114,'animal_115':animal_115,
                    'animal_116':animal_116,'animal_117':animal_117,'animal_118':animal_118,'animal_119':animal_119,
                    'animal_120':animal_120,'animal_121':animal_121,'animal_122':animal_122,'animal_123':animal_123,
                    'animal_124':animal_124,'animal_125':animal_125,'animal_126':animal_126,'animal_127':animal_127,
                    'animal_128':animal_128,'animal_129':animal_129,'animal_130':animal_130,'animal_131':animal_131,
                    'animal_132':animal_132,'animal_133':animal_133,'animal_134':animal_134,'animal_135':animal_135,
                    'animal_136':animal_136,'animal_137':animal_137,'animal_138':animal_138,'animal_139':animal_139,
                    'animal_140':animal_140,'animal_141':animal_141,'animal_142':animal_142,'animal_143':animal_143,
                    'animal_144':animal_144,'animal_145':animal_145,'animal_146':animal_146,'animal_147':animal_147,
                    'animal_148':animal_148,'animal_149':animal_149,'animal_150':animal_150,'animal_151':animal_151,
                    'animal_152':animal_152,'animal_153':animal_153,'animal_154':animal_154,'animal_155':animal_155,
                    'animal_156':animal_156,'animal_157':animal_157,'animal_158':animal_158,'animal_159':animal_159,
                    'animal_160':animal_160,'animal_161':animal_161,'animal_162':animal_162,'animal_163':animal_163,
                    'animal_164':animal_164,'animal_165':animal_165,'animal_166':animal_166,'animal_167':animal_167,
                    'animal_168':animal_168,'animal_169':animal_169,'animal_170':animal_170,'animal_171':animal_171,
                    'animal_172':animal_172,'animal_173':animal_173,'animal_174':animal_174,'animal_175':animal_175,
                    'animal_176':animal_176,'animal_177':animal_177,'animal_178':animal_178,'animal_179':animal_179,
                    'animal_180':animal_180,'animal_181':animal_181,'animal_182':animal_182,'animal_183':animal_183,
                    'animal_184':animal_184,'animal_185':animal_185,'animal_186':animal_186,'animal_187':animal_187,
                    'animal_188':animal_188,'animal_189':animal_189,'animal_190':animal_190,'animal_191':animal_191,
                    'animal_192':animal_192,'animal_193':animal_193,'animal_194':animal_194,'animal_195':animal_195,
                    'animal_196':animal_196,'animal_197':animal_197,'animal_198':animal_198,'animal_199':animal_199,
                    'animal_200':animal_200,'animal_201':animal_201,'animal_202':animal_202,'animal_203':animal_203,
                    'animal_204':animal_204,'animal_205':animal_205,'animal_206':animal_206,'animal_207':animal_207,
                    'animal_208':animal_208,'animal_209':animal_209,'animal_210':animal_210,'animal_211':animal_211,
                    'animal_212':animal_212,'animal_213':animal_213,'animal_214':animal_214,'animal_215':animal_215,
                    'animal_216':animal_216,'animal_217':animal_217
                    }

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
x = 0

for i in range(0, 400):
    if i % 20 == 0:
        x += 1
    g = Particle(False,Vector(x * 500, (i % 20) * 500), Vector(0, 0),0,0,0,0,'grass01',spriteDictionary,0.0001,False,False)

    g.spriteSheet.setRow(1, 1, 1, 1, 1, 1)

    particle_set_bottom.add(g)

dragon=Particle(True,Vector(0,2500),Vector(0,150),150,0,0,0,'whiteDragon',spriteDictionary,25,False,False)
dragon.spriteSheet.setRow(5,4,1,1,5,4)
dragon.move(Vector(10000,2500))
moving_set.add(dragon)

dragon2=Particle(True,Vector(0,2000),Vector(0,150),150,0,0,0,'greenDragon',spriteDictionary,25,False,False)
dragon2.spriteSheet.setRow(5,4,1,1,5,4)
dragon2.move(Vector(10000,2500))


tree=Particle(True,Vector(2500,2500),Vector(0,0),200,0,0,0,'tree',spriteDictionary,0.1,False,False)
tree.spriteSheet.setRow(4,15,1,1,4,15)
