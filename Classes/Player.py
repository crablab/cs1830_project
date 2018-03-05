import json
import time
from Classes.Particle import Particle
from Classes.Settings import SPRITE_FPS
from Classes.Vector import Vector


class Player:
    def __init__(self, pos, vel,maxVel, angle,dimensions,radius,spriteKey,spriteDictionary,spriteFps, idPlayer):
        # id's
        self.idClass = 4
        self.idPlayer = idPlayer
        # non-vectors (attributes)
        self.maxVel = maxVel

        # vectors
        #Sprite Attributes
        self.spriteState = 0
        self.currentTime = 0


        #ParticleClass
        self.particle=Particle(pos,vel,maxVel,0,angle,radius,spriteKey,spriteDictionary,spriteFps,False,False)

    def walkUp(self):

        self.particle.spriteSheet.setRow(21,13,9,1,9,9)

    def walkLeft(self):
        self.particle.spriteSheet.setRow(21,13,10,1,9,9)

    def walkDown(self):
        self.particle.spriteSheet.setRow(21,13,11,1,9,9)

    def walkRight(self):
        self.particle.spriteSheet.setRow(21,13,12,1,9,9)

    def fireRight(self):
        self.particle.spriteSheet.setRow(21,13,20,1,16,13)
    def fireDown(self):
        self.particle.spriteSheet.setRow(21,13,19,1,16,13)
    def fireLeft(self):
        self.particle.spriteSheet.setRow(21,13,18,1,16,13)
    def fireUp(self):
        self.particle.spriteSheet.setRow(21,13,17,1,16,13)

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


        if (self.spriteState>0 and self.spriteState<5) and self.particle.vel.getX() !=0 and self.particle.vel.getY()!=0:
            self.particle.spriteSheet.update()
        elif self.particle.spriteSheet.hasLooped and self.spriteState>4:
            self.defaultWalkingDirection()

        elif (self.particle.spriteSheet.currentColumn-self.particle.spriteSheet.startColumn) < (self.particle.spriteSheet.endColumn-self.particle.spriteSheet.startColumn)and self.spriteState>4:
            self.particle.spriteSheet.update()



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
