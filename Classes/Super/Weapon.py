import time, configparser

from Classes.Middle.Particle import Particle

config = configparser.ConfigParser()
config.read_file(open('Classes/config'))


# exact copy of player but used for monsters and no preset animations
class Weapon:
    def __init__(self, pos, vel, nextPosTime, nextPos, maxVel, angle, radius, spriteKey, spriteDictionary, spriteFps,
                 idObject, numRows, numColumns, startRow, startColumn, endRow, endColumn, removeOnVelocity0,
                 removeOnAnimationLoop, damage):
        # id's
        self.remove = False
        self.idClass = 5
        self.idPlayer=0#set on weapon creation.
        self.idObject = idObject
        self.updateSprite=True
        # non-vectors (attributes)
        self.damage = damage
        self.applied=False
        # vectors

        # Sprite Attributes
        self.currentTime = 0
        self.removeOnVelocity0 = removeOnVelocity0
        self.removeOnAnimationLoop = removeOnAnimationLoop

        # sub class
        self.particle = Particle(self.updateSprite, pos, vel, nextPosTime, nextPos, maxVel, 0, angle, radius, spriteKey,#0 is the range, as this is a weapon, no need.
                                 spriteDictionary, spriteFps,
                                 self.removeOnVelocity0, self.removeOnAnimationLoop,
                                 self.idObject, numRows, numColumns,
                                 startRow, startColumn, endRow,
                                 endColumn)

    def recieve(self, nextPos, nextPosTime, maxVel, angle, spriteKey,
                fps, numRows, numColumns, startRow, startColumn, endRow, endColumn, radius, spriteDictionary):

        self.particle.recieve(nextPos, nextPosTime, maxVel, 0, angle, True, spriteKey, fps, numRows,
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
        data = {

            'pos': {'x': self.particle.pos.x, 'y': self.particle.pos.y},
            'vel': {'x': self.particle.vel.x, 'y': self.particle.vel.y},
            'nextPosTime': self.particle.nextPosTime,
            'nextPos': {'x': self.particle.nextPos.x, 'y': self.particle.nextPos.y},

            'maxVel': self.particle.maxVel,
            'angle': self.particle.angle,
            'radius': self.particle.radius,
            'spriteKey': self.particle.spriteKey,
            'fps': self.particle.spriteSheet.fps,
            'idObject': self.idObject,

            'removeOnVelocity0': self.removeOnVelocity0,
            'removeOnAnimationLoop': self.removeOnAnimationLoop,

            'idClass': self.idClass,

            'currentTime': self.currentTime,

            'numColumns': self.particle.spriteSheet.numColumns,
            'numRows': self.particle.spriteSheet.numRows,
            'startColumn': self.particle.spriteSheet.startColumn,
            'startRow': self.particle.spriteSheet.startRow,
            'endRow': self.particle.spriteSheet.endRow,
            'endColumn': self.particle.spriteSheet.endColumn,
            'damage': self.damage}

        return data
