#to read data into dictionary: data = json.loads(<json File>, object_hook=lambda d: namedtuple('<Object Name For Reference>', d.keys())(*d.values()))
from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Grass import Grass
from Classes.Particle import Particle
from Classes.Player import Player

from collections import namedtuple
import json

def getCam(arr):
    obj=Camera(Vector(arr.origin.x,arr.origin.y),Vector(arr.dim.x,arr.dim.y))
    return obj
def getGrass(arr):
    obj = Grass(Vector(arr.pos.x, arr.pos.y), arr.idP)
    return obj
def getParticle(arr):
    obj = Particle(Vector(arr.pos.x, arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.angle,arr.radius)
    return obj
def getPlayer(arr):
    obj = Player(Vector(arr.pos.x, arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.angle)
    return obj
def getVector(arr):
    obj = Vector(arr.x,arr.y)
    return obj

def GetObject(j):
    arr = json.loads(j, object_hook=lambda d: namedtuple('arr', d.keys())(*d.values()))
    if arr.id==1:
        return getCam(arr)
    elif arr.id==2:
        return getGrass(arr)
    elif arr.id==3:
        return getParticle(arr)
    elif arr.id==4:
        return getPlayer(arr)
    elif arr.id==5:
        return getVector(arr)
    else:
        return "error"

