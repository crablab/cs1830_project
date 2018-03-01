from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_keys, simplegui_lib_fps

import random
import copy
import pygame
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
#image = simpleguics2pygame.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def getP(self):
        return (self.x, self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def copy(self):
        v = Vector(self.x, self.y)
        return v

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def multiplyVector(self, other):
        self.x *= other.x
        self.y *= other.y
        return self
    def divide(self, k):
        self.x /= k
        self.y /= k
        return self

    def divideVector(self, other):
        self.x /= other.x
        self.y /= other.y
        return self
    def normalize(self):
        return self.divide(self.length())

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Returns the squared length of the vector
    def lengthSq(self):
        return self.x ** 2 + self.y ** 2

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.mult(2 * self.dot(normal))
        self.subtract(n)
        return self

    def rotate(self, angle):
        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return self
    def angle(self, other):
        return math.acos((self.dot(other)) / (self.length() * other.length()))
class Particle:
    def __init__(self, pos, vel, angle,radius):
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.radius = radius

    def draw(self, canvas,width):
        canvas.draw_circle(self.pos.getP(), self.radius/width, 1, "Pink", "Pink")

    def bounce(self, normal):
        self.vel.reflect(normal)

    def update(self):
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)
    def copy(self):
        p=Particle(self.pos,self.vel,self.angle)
        return(p)
    def transform(self,cam):
        #get Distance

        dist=self.pos.copy()
        dist.subtract(cam.origin)

        #get ratio
        ratio=dist.divideVector(cam.dim.copy().divide(2))

        #multiply ration on real screen
        self.pos=ratio.multiplyVector(cam.dimCanv.copy().divide(2))
        self.pos.add(cam.dimCanv.copy().divide(2))



class Sprite:
    def __init__(self, image):
        self.image = simpleguics2pygame.load_image(image)

        self.dim = Vector(self.image.get_width()*SpriteSize,self.image.get_height()*SpriteSize)


    def draw(self, canvas, cam, pos):
        # get Distance
        dist = pos.copy()
        dist.subtract(cam.origin)
        # get ratio
        ratio = dist.divideVector(cam.dim.copy().divide(2))
        # multiply ration on real screen
        pos = ratio.multiplyVector(cam.dimCanv.copy().divide(2))
        pos.add(cam.dimCanv.copy().divide(2))
        print('yo')
        imgDim=(self.dim.copy().divide(cam.dim.x).getP())
        imgCenter = tuple(ti/2 for ti in imgDim)
        canLoc=pos.getP()
        canvas.draw_image(self.image,[self.image.get_width()//2,self.image.get_height()//2],[self.image.get_width(),self.image.get_width()], canLoc,imgDim)



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

class Player:
    def __init__(self, pos, vel, angle):
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.radius = 10

    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, "White", "White")

    def bounce(self, normal):
        self.vel.reflect(normal)

    def update(self):
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)


