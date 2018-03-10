import random
import configparser
import uuid
from Classes.Objects import env_l1_set,spriteDictionary,getUid,env_l2_set
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Settings import MAP_HEIGHT,MAP_WIDTH

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

    for x in range(1,int(width/500)):
        for y in range(1,int(height/500)):
            winner=0
            dh=random.randrange(80,100)/100
            dl=random.randrange(1,30)/100
            mh=random.randrange(60,100)/100
            ml=random.randrange(1,50)/100
            prob=0
            if y>(height/500)*dh or y<(height/500)*dl or x>(width/500)*dh or x<(width/500)*dl:
                prob=50
                grass=getRandomString('en_l1_gs_d_',5)

            elif (y > (height / 500) * mh or y < (height / 500) *ml) or ( x > (width / 500) * mh or x < ( width / 500) * ml):
                prob=25
                winner=2
                grass = getRandomString('en_l1_gs_m_',5)
            else :
                prob=5
                winner=1
                grass = getRandomString('en_l1_gs_l_',5)
            #Grass
            pos=Vector(x*500,y*500)
            env_l1_set.add(Particle(False, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0,
                     grass, spriteDictionary, 0.0001, False, False, getUid(), 1, 1, 1, 1, 1, 1))

            px=pos.getX()
            py=pos.getY()
            for z in range(10):
                for z1 in range(10):
                    pos=Vector(z*50-250,z1*50-250)
                    num=random.randrange(0,1000)
                    if num>prob:
                        pass
                    else:
                        pos.add(Vector(px,py))

                        tree=getRandomString('en_l2_ts_1x1_',22)
                        env_l2_set.add(Particle(False, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0,
                                                tree, spriteDictionary, 0.0001, False, False, getUid(), 1, 1, 1, 1, 1, 1))
