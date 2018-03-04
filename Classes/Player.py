import json
import time
from Classes.CharacterSprite import Character
from Classes.Settings import SPRITE_FPS
from Classes.Vector import Vector


class Player:
    def __init__(self, pos, vel, angle, idP):
        # id's
        self.id = 4
        self.idP = idP
        # non-vectors (attributes)
        self.maxVel = 100
        self.angle = angle
        self.radius = 10  # multiply by 200
        # vectors
        self.pos = pos
        self.vel = vel
        self.nextPos = Vector(0, 0)
        self.nextPosTime = 0
        # sprites
        self.character = Character(self.pos, 1)
        self.action = 0
        self.time = 0
        self.updateTime=0

    def walkUp(self):

        self.character.setRow(9, 1, 9, 13, 21)

    def walkLeft(self):
        self.character.setRow(10, 1, 9, 13, 21)

    def walkDown(self):
        self.character.setRow(11, 1, 9, 13, 21)

    def walkRight(self):
        self.character.setRow(12, 1, 9, 13, 21)
    def fireRight(self):

        self.character.setRow(20, 1, 9, 13, 21)

    def setAction(self, id):
        self.action = id
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
            self.action = id

    def draw(self, canvas, cam, actionId):


        self.character.draw(canvas, cam,self.pos)


    def bounce(self, normal):
        self.vel.reflect(normal)

    def move(self, pos):
        self.nextPos = pos
        self.timeTo()

        self.vel.negate()

    def update(self):
        if self.pos.copy().subtract(self.nextPos).dot(self.vel) > 0:
            self.vel.multiply(0)
        x, y = self.pos.copy().distanceToVector(self.nextPos)
        dist = Vector(x, y)
        dist.negate()

        if self.nextPosTime - time.time() < 0:
            self.pos = self.nextPos
        else:

            self.vel = dist.divide(self.nextPosTime - time.time())
            self.vel.multiply(time.time() - self.time)
            self.pos.add(self.vel)

        self.time = time.time()

        if self.time-self.updateTime>SPRITE_FPS:
            print(self.action)
            if (self.action>0 and self.action<5) and self.vel.getX !=0 and self.vel.getY()!=0:
                self.character.update()
            elif self.character.column==self.character.numPictures-1 and self.action>4:
                self.chooseWalkingDirection()
            elif self.character.column < self.character.numPictures and self.action>4:
                self.character.update()

            self.updateTime=self.time
    def chooseWalkingDirection(self):
        x,y=self.pos.copy().distanceToVector(self.nextPos)
        if y < 0:
            self.setAction(3)
        if y > 0:
            self.setAction(1)
        if y != 0:
            if (x + y) / y > 2 and y < 0:
                self.setAction(4)
                pass
            if (x + y) / y < 0 and y < 0:
                self.setAction(2)
                pass
    def turn(self, angle):
        self.angle += angle

    def timeTo(self):
        self.nextPosTime = time.time() + self.pos.copy().distanceTo(self.nextPos) / self.maxVel

    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
