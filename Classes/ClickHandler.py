import pygame

from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Objects import mouse, particle_set_bottom, particle_set_middle, particle_set_top, player_list, cam, \
    adjustment, spriteDictionary,moving_set
from Classes.Settings import PARTICLE_VELOCITY, PARTICLE_RADIUS, PARTICLE_MAX_RANGE
import time
import math
import uuid



def checkClick():
    left, middle, right = pygame.mouse.get_pressed()

    # LEFT KEY
    if left and mouse.releasedL:
        mouse.pressL()
        for player in player_list:

            player.particle.spriteSheet.resetLoop()
            x, y = pygame.mouse.get_pos()
            vector = Vector(x, y)
            vector.subtract(adjustment)  # simplegui-pygame screen position adjustment
            vector.transformFromCam(cam)

            particle = Particle(True,player.particle.pos.copy(), player.particle.vel.copy(),PARTICLE_VELOCITY,PARTICLE_MAX_RANGE,0,PARTICLE_RADIUS,'arrow',spriteDictionary,0.001,True,False,str(uuid.uuid4()))

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


    elif left:
        pass
    elif not left and not mouse.releasedL:
        mouse.releaseL()

    # RIGHT KEY
    if right and mouse.releasedR:
        mouse.pressR()
        for player in player_list:
            x, y = pygame.mouse.get_pos()
            vector = Vector(x, y)
            vector.subtract(adjustment)
            vector.transformFromCam(cam)
            player.move(vector)
            player.defaultWalkingDirection()

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
