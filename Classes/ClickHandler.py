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

        for player in player_list:


            if playerId==player.idObject and not player.hasFired:
                #GET CLICK POSITION AND ADJUST FROM CANVAS TO WORLD
                x, y = pygame.mouse.get_pos()
                player.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)#REFER TO CLASSES.OBJECTS ADJUSTMENT, (PYGAME SIMPLE GUI COMPATIBILITY ADJUSTMENT)
                player.hasFired = True
                player.particle.spriteSheet.resetLoop()

                # ARCHERY
                if player.weapon==1:

                    player.setCorrectAnimation(2)
                    vector= player.clickPosition.copy()

                    if player.range<10: pass
                    #SET WEAPON
                    weapon=Weapon(player.particle.pos.copy(), player.particle.vel.copy(), 0, player.particle.pos.copy(), 0, 0, 0, getRandomArrow(player.range), spriteDictionary, 1, getUid(), 1, 1, 1, 1, 1, 1, True, False, player.range)
                    #DEFINE RANGE AND VEL
                    weapon.particle.maxRange= player.range / 2
                    weapon.particle.maxVel= player.range / 2
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
                if player.weapon == 2:

                    player.hasFired = True
                    player.particle.spriteSheet.resetLoop()
                    player.setCorrectAnimation(3)

                    # simplegui-pygame screen position adjustment


                    #SET MAGIC SPRITE ATTACK ANIMATION
                    numRows,numCol,startRow,startCol,endRow,endCol,key=getRandomMagicWeapon(player.magic)
                    #SET MAGIC SPRITE WEAPON WITH The above
                    print(numRows,numCol,key)
                    weapon = Weapon(player.clickPosition.copy(), Vector(0, 0), 0,
                                    player.clickPosition.copy(), 0, 0, 0, key, spriteDictionary,
                                    20, getUid(), numRows, numCol, startRow, startCol, endRow, endCol, False, True, player.magic)
                    #BIND SPRITE TO PLAYER and PLAYER TO SPRITE to remember who kills who
                    weapon.idPlayer=player.idObject
                    player.magicId=weapon.idObject

                    weapon_set.add(weapon)



                    # SET MAGIC SPRITE CASTING ANIMATION USE PARTICLE CLASS ADD TO VISUAL SET
                    #SHIFT ALL MAGIC SPRITES UP FOR PLAYER AS HE IS SMALL
                    pos=player.particle.pos.copy()
                    pos.y-=30
                    numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMagicCast(player.magic)
                    particle=Particle(True,pos,Vector(0,0),0,pos,0,0,0,0,key,spriteDictionary,20,False,True,getUid(),numRows,numCol,startRow,startCol,endRow,endCol)
                    visual_set.add(particle)


                # MAGIC
                if player.weapon == 3:
                    player.hasFired = True
                    player.particle.spriteSheet.resetLoop()
                    player.setCorrectAnimation(3)
                    vector = player.clickPosition.copy()


                    # SET MAGIC SPRITE SHOWOFF ANIMATION USE PARTICLE CLASS ADD TO VISUAL SET
                    # SHIFT ALL MAGIC SPRITES UP FOR PLAYER AS HE IS SMALL AND ADD A VERTICAL VELOCITY
                    pos = player.particle.pos.copy()
                    pos.y -= 30
                    numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomShowOff(player.magic)

                    particle = Particle(True, pos,Vector(0,0), 0, pos, 20,300, 0, 0, key, spriteDictionary, 20,
                                        False, True, getUid(), numRows, numCol, startRow, startCol, endRow, endCol)
                    print(player.particle.pos.copy().subtract(Vector(0,100)))
                    particle.moveRange(player.particle.pos.copy().subtract(Vector(0, 100)))
                    print(particle.nextPos)
                    print(player.particle.pos)
                    # particle.vel.negate()#bug, don't know why, needs negation...
                    visual_set.add(particle)


                if player.hasFired:
                    player.particle.vel.multiply(0)
                    player.particle.nextPosTime = time.time()
                    player.particle.nextPos = player.particle.pos


        mouse.pressL()
    elif left:
        pass
    elif not left and not mouse.releasedL:
        mouse.releaseL()

    # RIGHT KEY
    if right and mouse.releasedR:
        mouse.pressR()

        for player in player_list:

            if player.idObject==playerId and player.hasFired==False:
                 #force finish fireing
                x, y = pygame.mouse.get_pos()
                player.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)
                player.setCorrectAnimation(1)
                vector = player.clickPosition.copy()
                player.move(vector)



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
