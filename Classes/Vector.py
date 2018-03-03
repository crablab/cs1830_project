from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_keys, simplegui_lib_fps
import random
import copy
import pygame
import math
import json

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id=6
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def negate(self):
        self.multiply(-1)
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
    def size(self):
        return self.x+self.y
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

    def transform(self,cam):

        self.subtract(cam.dimCanv.copy().divide(2))
        ratio = cam.dim.copy().divideVector(cam.dimCanv)
        self.multiplyVector(ratio)
        self.add(cam.origin)


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)