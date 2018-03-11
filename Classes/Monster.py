import json, time, uuid, configparser

from Classes.Particle import Particle
from Classes.Settings import SPRITE_FPS #this never seems to be used?
config = configparser.ConfigParser()
config.read_file(open('Classes/config'))
from Classes.Vector import Vector

#exact copy of player but used for monsters and no preset animations
class Monster:
    def __init__(self, pos, vel, nextPosTime, nextPos, maxVel, angle, radius, spriteKey, spriteDictionary, spriteFps,
                 idObject, hasFired,
                 clickPosition, spriteState, numRows, numColumns, startRow, startColumn, endRow, endColumn,reviveTime,operationRange,attackRange,tier):
        # id's
        self.remove = False
        self.idClass = 4
        self.idObject = idObject
        self.magicId = 0 #this is a space to attach a particle object id so we can link it to this class if there is one.
        # non-vectors (attributes)
        self.reviveTime=reviveTime
        self.operationRange=operationRange
        self.attackRange=attackRange

        self.life = 10000*(tier**3)
        self.range = 1000*(tier**3)
        self.melee = 1000*(tier**3)
        self.magic = 1000*(tier**3)

        # vectors
        self.clickPosition = clickPosition
        # Sprite Attributes
        self.spriteState = spriteState
        self.currentTime = 0
        self.hasFired = hasFired


        #sub class
        self.particle = Particle(True, pos, vel, nextPosTime, nextPos, maxVel, 0, angle, radius, spriteKey,
                                 spriteDictionary, spriteFps,
                                 False, False, self.idObject, numRows, numColumns, startRow, startColumn, endRow,
                                 endColumn)

    def recieve(self, hasFired, clickPosition, nextPos, nextPosTime, maxVel, maxRange, angle, updateSprite, spriteKey,
                fps, numRows, numColumns, startRow, startColumn, endRow, endColumn, radius, spriteDictionary,life,range,melee,magic,magicId):
        self.magicId=magicId
        self.life=life
        self.melee=melee
        self.range=range
        self.magic=magic
        self.hasFired = hasFired
        self.clickPosition = clickPosition
        self.particle.recieve(nextPos, nextPosTime, maxVel, maxRange, angle, updateSprite, spriteKey, fps, numRows,
                              numColumns, startRow, startColumn, endRow, endColumn, radius, spriteDictionary)

    def draw(self, canvas, cam):

        self.particle.draw(canvas, cam)

    def move(self, pos):
        self.particle.move(pos)

    def update(self):
        self.particle.update()
        self.currentTime = time.time()

    def turn(self, angle):
        self.particle.angle += angle

    def encode(self):

        data = {'spriteState': self.spriteState,
                'clickPosition': {'x': self.clickPosition.x, 'y': self.clickPosition.y}, 'hasFired': self.hasFired,
                'idObject': self.idObject, 'idClass': self.idClass,
                'pos': {'x': self.particle.pos.x, 'y': self.particle.pos.y},
                'vel': {'x': self.particle.vel.x, 'y': self.particle.vel.y}, 'maxVel': self.particle.maxVel,
                'angle': self.particle.angle, 'radius': self.particle.radius, 'spriteKey': self.particle.spriteKey,
                'currentTime': self.currentTime,
                'nextPos': {'x': self.particle.nextPos.x, 'y': self.particle.nextPos.y},
                'nextPosTime': self.particle.nextPosTime,
                'fps': self.particle.spriteSheet.fps, 'remove': self.remove,
                'updateSprite': self.particle.updateSprite, 'maxRange': self.particle.maxRange,
                'numColumns': self.particle.spriteSheet.numColumns,
                'numRows': self.particle.spriteSheet.numRows, 'startColumn': self.particle.spriteSheet.startColumn,
                'startRow': self.particle.spriteSheet.startRow, 'endRow': self.particle.spriteSheet.endRow,
                'endColumn': self.particle.spriteSheet.endColumn,
                'magic':self.magic,'melee':self.melee,'range':self.range,'life':self.life,'magicId':self.magicId}

        return data
