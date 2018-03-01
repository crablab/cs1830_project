import SimpleGUICS2Pygame
from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_keys, simplegui_lib_fps

from Camera import Camera
from Sprite import Sprite
from Grass import Grass
from Particle import Particle
from Vector import Vector
from Player import Player
import random
import copy
import pygame
import math
USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
ParticleSize=2500
CAM_SENSITIVITY=5


class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line

grass = Grass(Vector(50,50))
p = Particle(Vector(250, 250), Vector(random.randint(-3, 3), random.randint(-3, 3)), 0,ParticleSize)
p1 = Particle(Vector(250, 100), Vector(random.randint(-3, 3), random.randint(-3, 3)), 0,ParticleSize)
cam=Camera(Vector(250,250),Vector(1000,1000))



def keyup(key):
    if key == simpleguics2pygame.KEY_MAP['r']:
        cam.zoomOut=False
    elif key == simpleguics2pygame.KEY_MAP['e']:
        cam.zoomIn=False
    elif key == simpleguics2pygame.KEY_MAP['right']:
        cam.moveRight=False
    elif key == simpleguics2pygame.KEY_MAP['left']:
        cam.moveLeft=False
    elif key == simpleguics2pygame.KEY_MAP['up']:
        cam.moveUp=False
    elif key == simpleguics2pygame.KEY_MAP['down']:
        cam.moveDown=False

def keydown(key):
    if key == simpleguics2pygame.KEY_MAP['r']:
        cam.zoomOut=True
    elif key == simpleguics2pygame.KEY_MAP['e']:
        if cam.dim.x>100 and cam.dim.y>100:
            cam.zoomIn=True
        else:
            cam.zoomIn=False
    elif key == simpleguics2pygame.KEY_MAP['right']:
        cam.moveRight = True
    elif key == simpleguics2pygame.KEY_MAP['left']:
        cam.moveLeft = True
    elif key == simpleguics2pygame.KEY_MAP['up']:
        cam.moveUp = True
    elif key == simpleguics2pygame.KEY_MAP['down']:
        cam.moveDown = True



def draw(canvas):

    cam.zoom()
    cam.move()
    pd1=copy.deepcopy(p1)
    pd=copy.deepcopy(p)
    pd1.transform(cam)
    pd.transform(cam)
    pd1.draw(canvas,cam.dim.x)
    pd.draw(canvas,cam.dim.x)
    g1=copy.deepcopy(grass)
    g1.draw(canvas, 3,cam)


frame = simpleguics2pygame.create_frame('A convex polygon domain', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
