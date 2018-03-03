import pygame
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Objects import mouse, particle_set,player,player_list,cam,adjustment
from Classes.Settings import PARTICLE_VELOCITY
import time

def checkClick():
    left, middle, right = pygame.mouse.get_pressed()


    # LEFT KEY
    if left and mouse.releasedL:
        mouse.pressL()
        for player in player_list:

            x,y=pygame.mouse.get_pos()
            vector=Vector(x,y)
            vector.subtract(adjustment)
            vector.transform(cam)
            particleV= player.pos.copy().subtract(vector)
            x=particleV.normalize().copy()

            particleV.multiply(PARTICLE_VELOCITY)
            particleV.negate()
            particleV.add(player.vel)
            particle=Particle(player.pos.copy(),particleV,player.angle,10)
            particle.pos.subtract(x.multiply(particle.radius*2))
            particle.time=time.time()
            particle_set.add(particle)



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
            vector.transform(cam)
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
