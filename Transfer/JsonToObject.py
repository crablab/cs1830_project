#to read data into dictionary: data = json.loads(<json File>, object_hook=lambda d: namedtuple('<Object Name For Reference>', d.keys())(*d.values()))
from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Objects import spriteDictionary,player2
from Classes.Particle import Particle
from Classes.Player import Player
from Classes.Objects import moving_set_external,moving_set, player_list
from Classes.Objects import cam
from collections import namedtuple
import json
import time

recieved_player_list=[]
recieved_particle_set=set()
### If exists local: update   if does not exist local: add      if boolean: remove  and on local then set boolean to False


def getCam(arr):
    obj=Camera(Vector(arr.origin.x,arr.origin.y),Vector(arr.dim.x,arr.dim.y))
    cam.recieve(obj)

def particle(arr):
  pass


def getPlayer(arr):
    if arr.idPlayer==2:
        player2.recieve(Player(Vector(arr.pos.x,arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.maxVel,arr.angle,arr.radius,arr.spriteKey,spriteDictionary,arr.spriteFps,arr.idObject,arr.idPlayer))





def getVector(arr):
    obj = Vector(arr.x,arr.y)
    return obj

def getObject(j):
    arr = json.loads(j, object_hook=lambda d: namedtuple('arr', d.keys())(*d.values()))
    print(arr.idClass)
    if arr.idClass==1:
        return getCam(arr)
    elif arr.idClass==2:
        return particle(arr)
    elif arr.idClass==3:
        return getPlayer(arr)
    elif arr.idClass==4:
        return getVector(arr)
    else:
        return "error"

