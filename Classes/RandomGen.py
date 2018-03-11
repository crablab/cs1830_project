import random
import configparser
import uuid
from Classes.Objects import env_l1_set,spriteDictionary,getUid,env_l2_list
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Settings import *

config = configparser.ConfigParser()
def getRandomString(string,range):
    num=random.randrange(1,range)
    if num==3:
        num=4
    return string+str(num)

def randomGrass():
    width,height=MAP_WIDTH,MAP_HEIGHT
    #Calculate some random grass values

    lightId=1
    medId=2
    darkId=3

    for x in range(1,int(width/512)):
        print(x)
        for y in range(1,int(height/512)):
            winner=0
            dh=random.randrange(80,100)/100
            dl=random.randrange(1,30)/100
            mh=random.randrange(60,100)/100
            ml=random.randrange(1,50)/100
            if y>(height/512)*dh or y<(height/512)*dl or x>(width/512)*dh or x<(width/512)*dl:
                grass=getRandomString('en_l1_gs_d_',5)

            elif (y > (height / 512) * mh or y < (height / 512) *ml) or ( x > (width / 512) * mh or x < ( width / 512) * ml):

                grass = getRandomString('en_l1_gs_m_',5)
            else :

                grass = getRandomString('en_l1_gs_l_',5)
            #Grass
            pos=Vector(x*512,y*512)
            print(pos)
            env_l1_set.add(Particle(False, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0,
                     grass, spriteDictionary, 0.0001, False, False, getUid(), 1, 1, 1, 1, 1, 1))



def randomTrees():
    width,height=MAP_WIDTH,MAP_HEIGHT
    #Calculate some random grass values

    lightId=1
    medId=2
    darkId=3
    cut=20
    print("------------------------")
    for y in range(1,int(height/cut)):
        for x in range(1,int(width/cut)):

            winner=0
            dh=random.randrange(80,100)/100
            dl=random.randrange(1,30)/100
            mh=random.randrange(60,100)/100
            ml=random.randrange(1,50)/100
            prob=0
            if y>(height/cut)*dh or y<(height/cut)*dl or x>(width/cut)*dh or x<(width/cut)*dl:
                prob=500

            elif (y > (height / cut) * mh or y < (height / cut) *ml) or ( x > (width / cut) * mh or x < ( width / cut) * ml):
                prob=250

            else :
                prob=125

            #Grass
            pos=Vector(x*cut,y*cut)


            num=random.randrange(0,TREE_PROB_RANGE)
            if num>prob:
                pass
            else:
                tree=getRandomString('en_l2_ts_1x1_',22)
                t1=Particle(False, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0,
                         tree, spriteDictionary, 0.0001, False, False, getUid(), 1, 1, 1, 1, 1, 1)
                t1.radius/=2

                env_l2_list.append(t1)

                #half tree radius to get nice coverage for updating choice intercection

            env_l2_list.reverse()
