#to read data into dictionary: data = json.loads(<json File>, object_hook=lambda d: namedtuple('<Object Name For Reference>', d.keys())(*d.values()))
from Classes.Camera import Camera
from Classes.Vector import Vector

from Classes.Particle import Particle
from Classes.Player import Player

from collections import namedtuple
import json

def getCam(arr):
    obj=Camera(Vector(arr.origin.x,arr.origin.y),Vector(arr.dim.x,arr.dim.y))
    return obj
def particleSquare(arr):
    obj = ParticleSquare(Vector(arr.pos.x, arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.angle,Vector(arr.dim.x,arr.dim.y),arr.spriteKey)
    return obj
def getParticleCircle(arr):
    obj = ParticleCircle(Vector(arr.pos.x, arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.angle,arr.radius,arr.spriteKey)
    return obj
def getPlayer(arr):
    obj = Player(Vector(arr.pos.x,arr.pos.y),Vector(arr.pos.x,arr.pos.y),arr.angle,Vector(arr.dim.x,arr.dim.y),arr.spriteKey,arr.idPlayer)
    return obj
def getVector(arr):
    obj = Vector(arr.x,arr.y)
    return obj

def GetObject(j):
    arr = json.loads(j, object_hook=lambda d: namedtuple('arr', d.keys())(*d.values()))
    if arr.idClass==1:
        return getCam(arr)
    elif arr.idClass==2:
        return particleSquare(arr)
    elif arr.idClass==3:
        return getParticleCircle(arr)
    elif arr.idClass==4:
        return getPlayer(arr)
    elif arr.idClass==5:
        return getVector(arr)
    else:
        return "error"

