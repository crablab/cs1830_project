#to read data into dictionary: data = json.loads(<json File>, object_hook=lambda d: namedtuple('<Object Name For Reference>', d.keys())(*d.values()))
from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Objects import spriteDictionary,playerId
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
    exists = False
    for player in player_list:
        if player.idObject==arr.idObject:
            exists=True
    if exists==False:
        player_list.append(player)

    for player in player_list:
        if player.idObject == arr.idObject and arr.idObject != playerId:
            player.recieve(Player(Vector(arr.pos.x,arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.maxVel,arr.angle,arr.radius,arr.spriteKey,spriteDictionary,arr.spriteFps,arr.idObject))
            print("changed")
        else:
            print("unchanged")



def getVector(arr):
    obj = Vector(arr.x,arr.y)
    return obj

def getObject(j):
    arr = json.loads(j, object_hook=lambda d: namedtuple('arr', d.keys())(*d.values()))
    print(arr.idClass)
    if arr.idClass==1:
        getCam(arr)
    elif arr.idClass==2:
        particle(arr)
    elif arr.idClass==3:
        getPlayer(arr)
    elif arr.idClass==4:
        getVector(arr)
    else:
        return "error"

