import json
import time
from Classes.Particle import Particle
from Classes.Settings import SPRITE_FPS
from Classes.Vector import Vector


class Player:
    def __init__(self, pos, vel, angle,dimensions,radius,spriteKey, idPlayer):
        # id's
        self.idClass = 4
        self.idPlayer = idPlayer
        # non-vectors (attributes)
        self.maxVel = 100

        # vectors
        #Sprite Attributes
        self.spriteState = 0
        self.currentTime = 0
        self.oldTime=0

        #ParticleClass
        self.particle=Particle(pos,vel,angle,dimensions,radius,spriteKey,self.maxVel,100,False,False)

    def walkUp(self):

        self.particle.sprite.setRow(9, 1, 9, 13, 21)

    def walkLeft(self):
        self.particle.sprite.setRow(10, 1, 9, 13, 21)

    def walkDown(self):
        self.particle.sprite.setRow(11, 1, 9, 13, 21)

    def walkRight(self):
        self.particle.sprite.setRow(12, 1, 9, 13, 21)

    def fireRight(self):
        self.particle.sprite.setRow(20, 1, 9, 13, 21)
    def fireDown(self):
        self.particle.sprite.setRow(19, 1, 9, 13, 21)
    def fireLeft(self):
        self.particle.sprite.setRow(18, 1, 9, 13, 21)
    def fireUp(self):
        self.particle.sprite.setRow(17, 1, 9, 13, 21)

    def setSpriteState(self, id):
        self.spriteState=id
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



    def draw(self, canvas, cam,spriteDictionary):

        self.particle.draw(canvas, cam,spriteDictionary)

    def move(self,pos):
        self.particle.move(pos)


    def update(self):
        self.particle.update()
        self.currentTime = time.time()

        #CORRECT SPRITE ROW AND UPDATE FPS
        if self.currentTime-self.oldTime>SPRITE_FPS:

            if (self.spriteState>0 and self.spriteState<5) and self.particle.vel.getX() !=0 and self.particle.vel.getY()!=0:
                self.particle.sprite.update()
            elif self.particle.sprite.hasLooped and self.spriteState>4:
                self.defaultWalkingDirection()

            elif self.particle.sprite.column < self.particle.sprite.numPictures and self.spriteState>4:
                self.particle.sprite.update()

            self.oldTime=self.currentTime

    def defaultWalkingDirection(self):
        x,y=self.particle.pos.copy().distanceToVector(self.particle.nextPos)
        if y < 0:
            self.setSpriteState(3)
        if y > 0:
            self.setSpriteState(1)
        if y != 0:
            if (x + y) / y > 2 and y < 0:
                self.setSpriteState(4)

            if (x + y) / y < 0 and y < 0:
                self.setSpriteState(2)

    def defaultFireingDirection(self,pos):
        x,y=self.particle.pos.copy().distanceToVector(pos)
        if y < 0:
            self.setSpriteState(6)
        if y > 0:
            self.setSpriteState(8)
        if y != 0:
            if (x + y) / y > 2 and y < 0:
                self.setSpriteState(5)

            if (x + y) / y < 0 and y < 0:
                self.setSpriteState(7)
    def turn(self, angle):
        self.particle.angle += angle



    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
