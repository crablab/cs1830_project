import json
import time
import uuid

from Classes.Particle import Particle
from Classes.Settings import SPRITE_FPS
from Classes.Vector import Vector


class Player:
    def __init__(self, pos, vel, nextPosTime, nextPos, maxVel, angle, radius, spriteKey, spriteDictionary, spriteFps,
                 idObject, hasFired,
                 clickPosition, spriteState, numRows, numColumns, startRow, startColumn, endRow, endColumn):
        # id's
        self.remove = False
        self.idClass = 3
        self.idObject = idObject

        # print(self.idObject)
        # non-vectors (attributes)

        # vectors
        self.clickPosition = clickPosition
        # Sprite Attributes
        self.spriteState = spriteState
        self.currentTime = 0
        self.hasFired = hasFired

        # ParticleClass
        self.particle = Particle(True, pos, vel, nextPosTime, nextPos, maxVel, 0, angle, radius, spriteKey,
                                 spriteDictionary, spriteFps,
                                 False, False, self.idObject, numRows, numColumns, startRow, startColumn, endRow,
                                 endColumn)

    def recieve(self, hasFired, clickPosition, nextPos, nextPosTime, maxVel, maxRange, angle, updateSprite, spriteKey,
                fps, numRows, numColumns, startRow, startColumn, endRow, endColumn, radius, spriteDictionary):

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

        if self.spriteState == 0:
            self.setCorrectAnimation()
        # CORRECT SPRITE ROW AND UPDATE FPS
        if self.hasFired and self.particle.spriteSheet.hasLooped:
            self.hasFired = False
            self.setCorrectAnimation()
        if self.particle.vel.getX() == 0 and self.particle.vel.getY() == 0 and not self.hasFired:
            # print("set column 1")
            self.particle.spriteSheet.currentColumn = 1

    def setCorrectAnimation(self):
        x, y = self.particle.pos.copy().distanceToVector(self.clickPosition)
        if y < 0:
            if self.hasFired:
                self.setSpriteState(6)

            else:
                self.setSpriteState(3)
        if y > 0:
            if self.hasFired:
                self.setSpriteState(8)

            else:
                self.setSpriteState(1)
        if y != 0:
            if (x + y) / y > 2 and y < 0:
                if self.hasFired:
                    self.setSpriteState(5)

                else:
                    self.setSpriteState(4)

            if (x + y) / y < 0 and y < 0:
                if self.hasFired:
                    self.setSpriteState(7)

                else:
                    self.setSpriteState(2)

    def walkUp(self):

        self.particle.spriteSheet.setRow(21, 13, 9, 1, 9, 9)

    def walkLeft(self):
        self.particle.spriteSheet.setRow(21, 13, 10, 1, 9, 9)

    def walkDown(self):
        self.particle.spriteSheet.setRow(21, 13, 11, 1, 9, 9)

    def walkRight(self):
        self.particle.spriteSheet.setRow(21, 13, 12, 1, 9, 9)

    def fireRight(self):
        self.particle.spriteSheet.setRow(21, 13, 20, 1, 16, 13)

    def fireDown(self):
        self.particle.spriteSheet.setRow(21, 13, 19, 1, 16, 13)

    def fireLeft(self):
        self.particle.spriteSheet.setRow(21, 13, 18, 1, 16, 13)

    def fireUp(self):
        self.particle.spriteSheet.setRow(21, 13, 17, 1, 16, 13)

    def setSpriteState(self, id):
        self.spriteState = id
        self.particle.spriteSheet.resetLoop()
        if id == 1:
            self.walkUp()
        elif id == 2:
            self.walkLeft()
        elif id == 3:
            self.walkDown()
        elif id == 4:
            self.walkRight()
        elif id == 5:
            self.fireRight()
        elif id == 6:
            self.fireDown()
        elif id == 7:
            self.fireLeft()
        elif id == 8:
            self.fireUp()

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
                'endColumn': self.particle.spriteSheet.endColumn}

        return data
