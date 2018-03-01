from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_keys, simplegui_lib_fps
import Vector
import random
import copy
import pygame
from Sprite import Sprite
import math
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
class Grass:

    image1= Sprite(USER_PATH+'img/grass/grass18.jpg')
    image2 = Sprite(USER_PATH+'img/grass/grass17.jpg')
    image3= Sprite(USER_PATH+'img/grass/grass16.jpg')
    image4 = Sprite(USER_PATH+'img/grass/grass19.jpg')

    def __init__(self, pos):

        self.pos=pos

    def draw(self,canvas,id,cam):
        if id==1:
            image=self.image1
        if id==2:
            image=self.image2
        if id==3:
            image=self.image3
        image=self.image4

        image.draw(canvas, cam,self.pos)

