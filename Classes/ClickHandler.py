import pygame
from Classes.RandomGen import getRandomString
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Objects import mouse,  player_list, cam, \
    adjustment, spriteDictionary,moving_set,playerId
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

            #ARCHERY
            if playerId==player1.idObject and not player1.hasFired and player1.weapon==1:
                x, y = pygame.mouse.get_pos()
                player1.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)
                player1.hasFired=True
                player1.particle.spriteSheet.resetLoop()
                player1.setCorrectAnimation()
                vector= player1.clickPosition.copy()
                 # simplegui-pygame screen position adjustment

                if player1.range<10: pass
                particle = Particle(True,player1.particle.pos.copy(), player1.particle.vel.copy(),0,Vector(0,0),int(config['PARTICLE']['PARTICLE_VELOCITY']),int(config['PARTICLE']['PARTICLE_MAX_RANGE']),0,int(config['PARTICLE']['PARTICLE_RADIUS']),'pr_t4_1',spriteDictionary,0.001,True,False,str(uuid.uuid4()),1,1,1,1,1,1)

                particle.moveRange(vector)
                particle.spriteSheet.setRow(1, 1, 1, 1, 1, 1)
                dist = particle.pos.copy().subtract(vector)
                dist.negate()
                if dist.length() != 0:
                    dist.normalize()
                particle.angle = dist.copy().getAngle(Vector(1, 0))
                x, y = particle.pos.copy().distanceToVector(vector)
                if y > 0:
                    particle.angle *= -1

                dist.multiply(particle.radius * 2)
                particle.pos.add(dist)

                moving_set.add(particle)
            # MAGIC
            if playerId == player1.idObject and not player1.hasFired and player1.weaponId == 2:
                x, y = pygame.mouse.get_pos()
                player1.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)
                player1.hasFired = True
                player1.particle.spriteSheet.resetLoop()
                player1.setCorrectAnimation()
                vector = player1.clickPosition.copy()
                # simplegui-pygame screen position adjustment

                particle = Particle(True, player1.particle.pos.copy(), player1.particle.vel.copy(), 0, Vector(0, 0),
                                    int(config['PARTICLE']['PARTICLE_VELOCITY']),
                                    int(config['PARTICLE']['PARTICLE_MAX_RANGE']), 0,
                                    int(config['PARTICLE']['PARTICLE_RADIUS']), 'arrow', spriteDictionary, 0.001,
                                    True, False, str(uuid.uuid4()), 1, 1, 1, 1, 1, 1)

                particle.moveRange(vector)
                particle.spriteSheet.setRow(1, 1, 1, 1, 1, 1)
                dist = particle.pos.copy().subtract(vector)
                dist.negate()
                if dist.length() != 0:
                    dist.normalize()
                particle.angle = dist.copy().getAngle(Vector(1, 0))
                x, y = particle.pos.copy().distanceToVector(vector)
                if y > 0:
                    particle.angle *= -1

                dist.multiply(particle.radius * 2)
                particle.pos.add(dist)

                moving_set.add(particle)
        mouse.pressL()
    elif left:
        pass
    elif not left and not mouse.releasedL:
        mouse.releaseL()

    # RIGHT KEY
    if right and mouse.releasedR:
        mouse.pressR()

        for player1 in player_list:

            if player1.idObject==playerId:
                x, y = pygame.mouse.get_pos()
                player1.clickPosition = Vector(x, y).subtract(adjustment).transformFromCam(cam)
                player1.setCorrectAnimation()
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
