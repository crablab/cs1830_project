import random
import configparser
import uuid
from Classes.Objects import env_l1_set, spriteDictionary, getUid, env_l2_list
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Settings import *

config = configparser.ConfigParser()


def getRandomString(string, range):
    num = random.randrange(1, range)
    if num == 3:
        num = 4
    return string + str(num)


def randomGrass():
    width, height = MAP_WIDTH, MAP_HEIGHT
    # Calculate some random grass values

    lightId = 1
    medId = 2
    darkId = 3

    for x in range(1, int(width / 512)):
        print(x)
        for y in range(1, int(height / 512)):
            winner = 0
            dh = random.randrange(80, 100) / 100
            dl = random.randrange(1, 30) / 100
            mh = random.randrange(60, 100) / 100
            ml = random.randrange(1, 50) / 100
            if y > (height / 512) * dh or y < (height / 512) * dl or x > (width / 512) * dh or x < (width / 512) * dl:
                grass = getRandomString('en_l1_gs_d_', 5)

            elif (y > (height / 512) * mh or y < (height / 512) * ml) or (
                    x > (width / 512) * mh or x < (width / 512) * ml):

                grass = getRandomString('en_l1_gs_m_', 5)
            else:

                grass = getRandomString('en_l1_gs_l_', 5)
            # Grass
            pos = Vector(x * 512, y * 512)
            print(pos)
            env_l1_set.add(Particle(False, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0,
                                    grass, spriteDictionary, 0.0001, False, False, getUid(), 1, 1, 1, 1, 1, 1))


def randomTrees():
    width, height = MAP_WIDTH, MAP_HEIGHT
    # Calculate some random grass values

    lightId = 1
    medId = 2
    darkId = 3
    cut = 20
    print("------------------------")
    for y in range(1, int(height / cut)):
        for x in range(1, int(width / cut)):

            winner = 0
            dh = random.randrange(80, 100) / 100
            dl = random.randrange(1, 30) / 100
            mh = random.randrange(60, 100) / 100
            ml = random.randrange(1, 50) / 100
            prob = 0
            if y > (height / cut) * dh or y < (height / cut) * dl or x > (width / cut) * dh or x < (width / cut) * dl:
                prob = 500

            elif (y > (height / cut) * mh or y < (height / cut) * ml) or (
                    x > (width / cut) * mh or x < (width / cut) * ml):
                prob = 250

            else:
                prob = 125

            # Grass
            pos = Vector(x * cut, y * cut)

            num = random.randrange(0, TREE_PROB_RANGE)
            if num > prob:
                pass
            else:
                tree = getRandomString('en_l2_ts_1x1_', 22)
                t1 = Particle(False, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0,
                              tree, spriteDictionary, 0.0001, False, False, getUid(), 1, 1, 1, 1, 1, 1)
                t1.radius /= 2

                env_l2_list.append(t1)

                # half tree radius to get nice coverage for updating choice intercection

            env_l2_list.reverse()


def getRandomArrow(range):
    if range > 50000:
        return (getRandomString('pr_t4_', 2))
    if range > 10000:
        return (getRandomString('pr_t3_', 4))
    if range > 1000:
        return (getRandomString('pr_t2_', 4))
    else:
        return ('pr_t1_1')




def getRandomMagicWeapon(magic):  # CANNOT USE RANDOM STRING AS ROWS AND COLUMNS ARE DIFFERENT FOR ANIMATED SPRITES
    range = magic//3500
    range+=3
    print("=========================================")
    print(range)
    if range > 13:
        range = 13
    num = random.randrange(0, range)
    print(range)
    print(magic)
    if num == 0:
        return (4, 5, 1, 1, 4, 5, 'ma_at_5x4_1')
    elif num == 1:
        return (4, 5, 1, 1, 5, 5, 'ma_at_5x4_2')

    elif num == 2:
        return (7, 5, 1, 1, 7, 5, 'ma_at_5x7_5')
    elif num == 3:
        return 5, 5, 1, 1, 5, 5, 'ma_at_5x5_1'
    elif num == 4:
        return (7, 5, 1, 1, 7, 5, 'ma_at_5x7_6')
    elif num == 5:
        return (6, 5, 1, 1, 6, 5, 'ma_at_5x6_1')
    elif num == 6:
        return (6, 5, 1, 1, 6, 5, 'ma_at_5x6_2')
    elif num == 7:
        return (6, 5, 1, 1, 6, 5, 'ma_at_5x6_3')
    elif num == 8:
        return (7, 5, 1, 1, 7, 5, 'ma_at_5x7_1')
    elif num == 9:
        return (7, 5, 1, 1, 7, 5, 'ma_at_5x7_4')
    elif num == 10:
        return (7, 5, 1, 1, 7, 5, 'ma_at_5x7_2')
    elif num == 11:
        return (7, 5, 1, 1, 7, 5, 'ma_at_5x7_3')
    elif num == 12:
        return (11, 5, 1, 1, 11, 5, 'ma_at_5x11_1')


def getRandomMagicCast(magic):  # CANNOT USE RANDOM STRING AS ROWS AND COLUMNS ARE DIFFERENT FOR ANIMATED SPRITES
    range = magic//3500
    range+=3
    print("=========================================")
    print(range)
    if range > 16:
        range = 16
    num = random.randrange(0, range)
    print(range)
    print(magic)
    if num == 0:
        return (4, 5, 1, 1, 4, 5, 'ma_ca_5x4_1')
    elif num == 1:
        return (4, 5, 1, 1, 4, 5, 'ma_ca_5x4_2')

    elif num == 2:
        return (4, 5, 1, 1, 4, 5, 'ma_ca_5x4_3')
    elif num == 3:
        return 7, 5, 1, 1, 7, 5, 'ma_ca_5x7_1'
    elif num == 4:
        return (7, 5, 1, 1, 7, 5, 'ma_ca_5x7_2')
    elif num == 5:
        return (7, 5, 1, 1, 7, 5, 'ma_ca_5x7_3')
    elif num == 6:
        return (7, 5, 1, 1, 7, 5, 'ma_ca_5x7_4')
    elif num == 7:
        return (7, 5, 1, 1, 7, 5,'ma_ca_5x7_5')
    elif num == 8:
        return (7, 5, 1, 1, 7, 5,'ma_ca_5x7_6')
    elif num == 9:
        return (7, 5, 1, 1, 7, 5,'ma_ca_5x7_7')
    elif num == 10:
        return (7, 5, 1, 1, 7, 5,'ma_ca_5x7_8')
    elif num == 11:
        return (7, 5, 1, 1, 7, 5, 'ma_ca_5x7_9')
    elif num == 12:
        return (7, 5, 1, 1, 7, 5, 'ma_ca_5x7_10')
    elif num == 13:
        return (7, 5, 1, 1, 7, 5,'ma_ca_5x7_11')
    elif num == 14:
        return (14, 5, 1, 1, 14, 5, 'ma_ca_5x14_1')
    elif num == 15:
        return (14, 5, 1, 1, 14, 5, 'ma_ca_5x14_2')


def getRandomShowOff(magic):
    range = magic // 3500
    range += 3
    print("=========================================")
    print(range)
    if range > 15:
        range = 15
    num = random.randrange(0, range)
    print(range)
    print(magic)
    if num == 0:
        return (4, 5, 1, 1, 4, 5, 'ma_sh_5x4_1')
    elif num == 1:
        return (4, 5, 1, 1, 4, 5, 'ma_sh_5x4_2')
    elif num == 2:
        return (4, 5, 1, 1, 4, 5, 'ma_sh_5x4_3')
    elif num == 3:
        return 4, 5, 1, 1, 4, 5, 'ma_sh_5x4_4'
    elif num == 4:
        return (6, 5, 1, 1, 6, 5, 'ma_sh_5x6_1')
    elif num == 5:
        return (6, 5, 1, 1, 6, 5, 'ma_sh_5x6_2')
    elif num == 6:
        return (6, 5, 1, 1, 6, 5, 'ma_sh_5x6_3')
    elif num == 7:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_1')
    elif num == 8:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_2')
    elif num == 9:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_3')
    elif num == 10:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_4')
    elif num == 11:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_5')
    elif num == 12:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_6')
    elif num == 13:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_7')
    elif num == 14:
        return (7, 5, 1, 1, 7, 5, 'ma_sh_5x7_8')


