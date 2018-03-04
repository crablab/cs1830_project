import pygame

from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Objects import mouse, particle_set, player_list, cam, adjustment
from Classes.Settings import PARTICLE_VELOCITY,PARTICLE_RADIUS,PARTICLE_MAX_RANGE
import time
import math


def checkClick():
    left, middle, right = pygame.mouse.get_pressed()

    # LEFT KEY
    if left and mouse.releasedL:
        mouse.pressL()
        for player in player_list:

            player.particle.sprite.resetLoop()
            x, y = pygame.mouse.get_pos()
            vector = Vector(x, y)
            vector.subtract(adjustment)  # simplegui-pygame screen position adjustment
            vector.transformFromCam(cam)

            particle = Particle(player.particle.pos.copy(), player.particle.vel.copy(),
                                      player.particle.angle,Vector(2*PARTICLE_RADIUS,2*PARTICLE_RADIUS), PARTICLE_RADIUS, 'arrow',
                                      PARTICLE_VELOCITY, PARTICLE_MAX_RANGE,True,False)
            particle.moveRange(vector)

            dist = particle.pos.copy().subtract(vector)
            dist.negate()
            dist.normalize()
            particle.angle=dist.copy().getAngle(Vector(1,0))
            x, y = particle.pos.copy().distanceToVector(vector)
            if y>0:
                particle.angle*=-1

            dist.multiply(particle.radius*2)
            particle.pos.add(dist)

            particle_set.add(particle)



            player.defaultFireingDirection(particle.nextPos)


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
