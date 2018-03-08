# to read data into dictionary: data = json.loads(<json File>, object_hook=lambda d: namedtuple('<Object Name For Reference>', d.keys())(*d.values()))
from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Objects import spriteDictionary, playerId
from Classes.Particle import Particle
from Classes.Player import Player
from Classes.Objects import moving_set_external, moving_set, player_list
from Classes.Objects import cam
from Classes.Settings import DEVELOPER_OPTIONS
from collections import namedtuple
import json
import time

recieved_player_list = []
recieved_particle_set = set()


### If exists local: update   if does not exist local: add      if boolean: remove  and on local then set boolean to False


def getCam(arr):
    obj = Camera(Vector(arr['origin']['x'], arr['origin']['y']), Vector(arr['dim']['x'], arr['dim']['y']))
    cam.recieve(obj)


def particle(arr):
    exists=False
    for particle in moving_set_external:
        if particle.idObject== arr['idObject']:
            exists=True
    if not exists:
        moving_set_external.add(Particle(arr['updateSprite'],Vector(arr['pos']['x'],arr['pos']['y']),Vector(arr['vel']['x'],arr['vel']['y']),
                                         arr['nextPosTime'],Vector(arr['nextPos']['x'], arr['nextPos']['y']), arr['maxVel'],arr['maxRange'],
                                         arr['angle'], arr['radius'],arr['spriteKey'],spriteDictionary,arr['fps'],arr['removeOnVelocity0'],
                                         arr['removeOnAnimationLoop'],arr['idObject'],arr['numRows'],arr['numColumns'],arr['startRow'],
                                         arr['startColumn'],arr['endRow'],arr['endColumn']))

    for particle in moving_set_external:
        if particle.idObject==arr['idObject']:
            particle.recieve(Vector(arr['nextPos']['x'], arr['nextPos']['y']),
                             arr['nextPosTime'],arr['maxVel'],arr['maxRange'],arr['angle'],
                             arr['updateSprite'],arr['spriteKey'],arr['fps'],arr['numRows'],
                             arr['numColumns'],arr['startRow'],arr['startColumn'],
                             arr['endRow'],arr['endColumn'],arr['radius'],spriteDictionary)


def getPlayer(arr):
    exists = False
    for player in player_list:

        if player.idObject == arr['idObject']:
            exists = True
    if not exists:
        player_list.append(
            Player(Vector(arr['pos']['x'],arr['pos']['y']),Vector(arr['vel']['x'],arr['vel']['y']),
                           arr['nextPosTime'],Vector(arr['nextPos']['x'], arr['nextPos']['y']), arr['maxVel'],
                           arr['angle'], arr['radius'], arr['spriteKey'], spriteDictionary,
                           arr['fps'],arr['idObject'], arr['hasFired'],
                           Vector(arr['clickPosition']['x'], arr['clickPosition']['y']),
                           arr['spriteState'],arr['numRows'],arr['numColumns'],arr['startRow'],arr['startColumn'],
                           arr['endRow'],arr['endColumn']))

    for player in player_list:
        if player.idObject == arr['idObject'] and arr['idObject'] != playerId:
            player.recieve(arr['hasFired'],Vector(arr['clickPosition']['x'], arr['clickPosition']['y']),Vector(arr['nextPos']['x'], arr['nextPos']['y']), arr['maxVel'],
                           arr['maxRange'], arr['angle'], arr['updateSprite'], arr['spriteKey'],
                arr['fps'], arr['numRows'], arr['numColumns'], arr['startRow'], arr['startColumn'], arr['endRow'], arr['endColumn'], arr['radius'], spriteDictionary)

def getVector(arr):
    obj = Vector(arr.x, arr.y)
    return obj


def getObject(j):
    print("------------------------")
    arr = json.loads(j)
    if (DEVELOPER_OPTIONS): print(arr)

    if(DEVELOPER_OPTIONS): print(arr)
    print(arr['idClass'])
    if arr['idClass'] == 1:
        getCam(arr)
    elif arr['idClass'] == 2:
        particle(arr)
    elif arr['idClass']== 3:
        getPlayer(arr)
    elif arr['idClass'] == 4:
        getVector(arr)
    else:
        return "No class for ID"
