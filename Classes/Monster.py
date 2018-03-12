import json, time, uuid, configparser
from SimpleGUICS2Pygame import simplegui_lib_draw
from Classes.Particle import Particle

from Classes.Settings import SPRITE_FPS, SHOW_BOUNDARIES #this never seems to be used?
config = configparser.ConfigParser()
config.read_file(open('Classes/config'))
from Classes.Vector import Vector

#exact copy of player but used for monsters and no preset animations
class Monster:
    def __init__(self, pos, vel, nextPosTime, nextPos, maxVel, angle, radius, spriteKey, spriteDictionary, spriteFps,
                 idObject, hasFired,
                 clickPosition, spriteState, numRows, numColumns, startRow, startColumn, endRow, endColumn,tier,aBack):
        # id's
        self.remove = False
        self.idClass = 4
        self.idObject = idObject
        self.magicId = 0 #this is a space to attach a particle object id so we can link it to this class if there is one.

        # non-vectors (attributes)
        self.operationOrigin=0
        self.operationRange=0
        self.attackRange=0
        self.followDistance=0
        self.tier=tier
        self.life = 0
        self.lifePrev=self.life
        self.range = 0
        self.melee = 0
        self.magic = 0
        self.tier = 0
        # vectors
        self.clickPosition = clickPosition
        # Sprite Attributes
        self.spriteState = spriteState
        self.currentTime = 0
        self.hasFired = hasFired
        self.fireCooldown=0
        self.followDistance = self.tier * 200  # arbitrary can't be bothered to set settings
        self.aBack=aBack
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

    def setSpriteState(self,state):
        self.spriteState=state
        if state == 1:    # FIRST HALF OF SPRITE SHEET GOING LEFT

            self.particle.spriteSheet.startRow=1
            self.particle.spriteSheet.endRow=self.particle.spriteSheet.numRows/2
            self.particle.spriteSheet.currentRow -= self.particle.spriteSheet.numRows / 2
        elif state == 2:  # SECOND HALF OF SPRITE SHEET GOING RIGHT

            self.particle.spriteSheet.endRow = self.particle.spriteSheet.numRows
            self.particle.spriteSheet.startRow = self.particle.spriteSheet.numRows / 2 + 1
            print("======================")
            print(self.particle.spriteSheet.startRow)
            print(self.particle.spriteSheet.endRow)
            print(self.particle.spriteSheet.numRows)
            print(self.particle.spriteSheet.numColumns)
            self.particle.spriteSheet.currentRow += self.particle.spriteSheet.numRows / 2

        if self.aBack and self.spriteState==1 and self.particle.spriteSheet.startColumn<self.particle.spriteSheet.endColumn:
                self.particle.spriteSheet.startColumn=self.particle.spriteSheet.numColumns
                self.particle.spriteSheet.endColumn=self.particle.spriteSheet.numColumns-self.particle.spriteSheet.endColumn
        elif not self.aBack and self.spriteState==1 and self.particle.spriteSheet.startColumn>self.particle.spriteSheet.endColumn:
            self.particle.spriteSheet.startColumn = 1
            self.particle.spriteSheet.endColumn = self.particle.spriteSheet.numColumns - self.particle.spriteSheet.endColumn
        elif not self.aBack and self.spriteState == 2 and self.particle.spriteSheet.startColumn < self.particle.spriteSheet.endColumn:
            self.particle.spriteSheet.startColumn = self.particle.spriteSheet.numColumns
            self.particle.spriteSheet.endColumn = self.particle.spriteSheet.numColumns - self.particle.spriteSheet.endColumn
        elif self.aBack and self.spriteState == 2 and self.particle.spriteSheet.startColumn > self.particle.spriteSheet.endColumn:
            self.particle.spriteSheet.startColumn = 1
            self.particle.spriteSheet.endColumn = self.particle.spriteSheet.numColumns - self.particle.spriteSheet.endColumn

    def draw(self, canvas, cam):

        self.particle.draw(canvas, cam)
        if SHOW_BOUNDARIES:
            simplegui_lib_draw.draw_rect(canvas, self.operationOrigin.copy().transformToCam(cam).subtract(
            self.operationRange.copy().divide(2).multiplyVector(cam.ratioToCam())).getP(),
                                     self.operationRange.copy().multiplyVector(cam.ratioToCam()).getP(), 1, 'White', fill_color=None)
    def move(self, pos):
        self.particle.move(pos)

    def update(self):
        print(self.particle.spriteSheet.currentRow,self.particle.spriteSheet.currentColumn, self.particle.spriteSheet.numRows,self.particle.spriteSheet.numColumns,self.particle.spriteSheet.startRow,self.particle.spriteSheet.startColumn,self.particle.spriteSheet.endRow,self.particle.spriteSheet.endColumn)
        self.particle.update()

        if self.hasFired:
            self.fireCooldown+=time.time()-self.currentTime
            if self.fireCooldown>5:
                self.hasFired=False
                self.fireCooldown=0

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
                'magic':self.magic,'melee':self.melee,'range':self.range,'life':self.life,'magicId':self.magicId,'tier':self.tier,'aBack':self.aBack}

        return data
