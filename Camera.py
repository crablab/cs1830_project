from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_keys, simplegui_lib_fps
import Vector
import random
import copy
import pygame
import math
from Vector import Vector
USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
#polygons
ParticleSize=2500

#Sprites:
SpriteSize=200
#CAMERA
CamMinDist=200
CAM_SENSITIVITY=5
class Camera:
    def __init__(self, origin, dim):
        self.origin = origin
        self.dim = dim
        self.dimCanv=Vector(CANVAS_WIDTH,CANVAS_HEIGHT)
        self.zoomIn=False
        self.zoomOut=False
        self.moveLeft=False
        self.moveRight=False
        self.moveUp=False
        self.moveDown=False

    def move(self):
        if self.moveUp==True:
            self.origin.add(Vector(0,-CAM_SENSITIVITY))
        if self.moveDown==True:
            self.origin.add(Vector(0,CAM_SENSITIVITY))

        if self.moveLeft == True:
            self.origin.add(Vector(-CAM_SENSITIVITY,0))
        if self.moveRight == True:
            self.origin.add(Vector(CAM_SENSITIVITY,0))


    def zoom(self):
        if self.zoomOut == True:
            self.dim.add(Vector(CAM_SENSITIVITY,CAM_SENSITIVITY ))
        if self.zoomIn == True and self.dim.x>CamMinDist and self.dim.y>CamMinDist:
            self.dim.add(Vector(-CAM_SENSITIVITY,-CAM_SENSITIVITY))

    def get(self):
        return(self.origin, self.height)
