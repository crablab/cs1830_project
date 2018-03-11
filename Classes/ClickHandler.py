import pygame
from Classes.RandomGen import getRandomString,getRandomArrow,getRandomMagicWeapon,getRandomMagicCast,getRandomShowOff

from Classes.Vector import Vector
from Classes.Objects import mouse,  player_list, cam, \
    adjustment, spriteDictionary,playerId,weapon_set,getUid,visual_set
from Classes.Weapon import Weapon
from Classes.Particle import Particle
from Classes.Settings import PARTICLE_VELOCITY, PARTICLE_RADIUS, PARTICLE_MAX_RANGE
import configparser, json, uuid, os, random
config = configparser.ConfigParser()
config.read_file(open('Classes/config'))

config.read_file(open('Classes/config'))
import time
import math
import uuid



def checkClick():
    left, middle, right = pygame.mouse.get_pressed()

    # LEFT KEY
    if left and mouse.releasedL:
        mouse.pressL()

        for player1 in player_list:


            if playerId==player1.idObject and not player1.hasFired:
                #GET CLICK POSITION AND ADJUST FROM CANVAS TO WORLD
                x, y = pygame.mouse.get_pos()
                player1.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)#REFER TO CLASSES.OBJECTS ADJUSTMENT, (PYGAME SIMPLE GUI COMPATIBILITY ADJUSTMENT)
                player1.hasFired = True
                player1.particle.spriteSheet.resetLoop()

                # ARCHERY
                if player1.weapon==1:

                    player1.setCorrectAnimation(2)
                    vector= player1.clickPosition.copy()

                    if player1.range<10: pass
                    #SET WEAPON
                    weapon=Weapon(player1.particle.pos.copy(),player1.particle.vel.copy(),0,player1.particle.pos.copy(),0,0,0,getRandomArrow(player1.range),spriteDictionary,1,getUid(),1,1,1,1,1,1,True,False,player1.range)
                    #DEFINE RANGE AND VEL
                    weapon.particle.maxRange=player1.range/2
                    weapon.particle.maxVel=player1.range/2
                    if weapon.particle.maxRange>1500:
                        weapon.particle.maxRange=1500
                    if weapon.particle.maxVel>1000:
                        weapon.particle.maxVel=1000
                    #MOVE WEAPON
                    weapon.particle.moveRange(vector)
                    #SET ANGLE (ARROW)
                    dist = weapon.particle.pos.copy().subtract(vector)
                    dist.negate()
                    if dist.length() != 0:
                        dist.normalize()
                    weapon.particle.angle = dist.copy().getAngle(Vector(1, 0))
                    x, y = weapon.particle.pos.copy().distanceToVector(vector)
                    if y > 0:
                        weapon.particle.angle *= -1
                    #ADJUST SPAWNIG DISTANCE AWAY FROM PLAYER
                    dist.multiply(weapon.particle.radius * 2)
                    weapon.particle.pos.add(dist)

                    #ADD WEAPON
                    weapon_set.add(weapon)

                # MAGIC
                if player1.weapon == 2:

                    player1.hasFired = True
                    player1.particle.spriteSheet.resetLoop()
                    player1.setCorrectAnimation(3)
                    vector = player1.clickPosition.copy()
                    # simplegui-pygame screen position adjustment


                    #SET MAGIC SPRITE ATTACK ANIMATION
                    numRows,numCol,startRow,startCol,endRow,endCol,key=getRandomMagicWeapon(player1.magic)
                    #SET MAGIC SPRITE WEAPON WITH The above
                    print(numRows,numCol,key)
                    weapon = Weapon(player1.clickPosition.copy(), Vector(0,0), 0,
                                    player1.clickPosition.copy(), 0, 0, 0,key, spriteDictionary,
                                    20, getUid(), numRows, numCol, startRow, startCol, endRow,endCol, False, True, player1.magic)
                    #BIND SPRITE TO PLAYER and PLAYER TO SPRITE to remember who kills who
                    weapon.idPlayer=player1.idObject
                    player1.magicId=weapon.idObject

                    weapon_set.add(weapon)



                    # SET MAGIC SPRITE CASTING ANIMATION USE PARTICLE CLASS ADD TO VISUAL SET
                    #SHIFT ALL MAGIC SPRITES UP FOR PLAYER AS HE IS SMALL
                    pos=player1.particle.pos.copy()
                    pos.y-=30
                    numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMagicCast(player1.magic)
                    particle=Particle(True,pos,Vector(0,0),0,pos,0,0,0,0,key,spriteDictionary,20,False,True,getUid(),numRows,numCol,startRow,startCol,endRow,endCol)
                    visual_set.add(particle)
                #
                # MAGIC
                if player1.weapon == 3:
                    player1.hasFired = True
                    player1.particle.spriteSheet.resetLoop()
                    player1.setCorrectAnimation(3)
                    vector = player1.clickPosition.copy()


                    # SET MAGIC SPRITE SHOWOFF ANIMATION USE PARTICLE CLASS ADD TO VISUAL SET
                    # SHIFT ALL MAGIC SPRITES UP FOR PLAYER AS HE IS SMALL AND ADD A VERTICAL VELOCITY
                    pos = player1.particle.pos.copy()
                    pos.y -= 30
                    numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomShowOff(player1.magic)
                    particle = Particle(True, pos,Vector(0,100), 0, pos, 0, 0, 0, 0, key, spriteDictionary, 20,
                                        False, True, getUid(), numRows, numCol, startRow, startCol, endRow, endCol)
                    visual_set.add(particle)


                if player1.hasFired:
                    player1.particle.vel.multiply(0)
                    player1.particle.nextPosTime = time.time()
                    player1.particle.nextPos = player1.particle.pos


        mouse.pressL()
    elif left:
        pass
    elif not left and not mouse.releasedL:
        mouse.releaseL()

    # RIGHT KEY
    if right and mouse.releasedR:
        mouse.pressR()

        for player1 in player_list:

            if player1.idObject==playerId and player1.hasFired==False:
                 #force finish fireing
                x, y = pygame.mouse.get_pos()
                player1.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)
                player1.setCorrectAnimation(1)
                vector = player1.clickPosition.copy()
                player1.move(vector)



    elif right:
        pass

    elif not right and not mouse.releasedR:

        mouse.releaseR()

    # MIDDLE KEY
    if middle and mouse.releasedM:
        mouse.pressM()
    elif middle:
        pass
    elif not middle and not mouse.releasedM:
        mouse.releaseM()
