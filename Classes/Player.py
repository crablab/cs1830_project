import json
import time
import uuid

from Classes.Particle import Particle
from Classes.Settings import SPRITE_FPS
from Classes.Vector import Vector


class Player:
    def __init__(self, pos, vel,maxVel, angle,radius,spriteKey,spriteDictionary,spriteFps, idObject,hasFired):
        # id's
        self.remove=False
        self.idClass = 3
        self.idObject=idObject

        #print(self.idObject)
        # non-vectors (attributes)
        self.maxVel = maxVel

        # vectors
        self.clickPosition=Vector(0,0)
        #Sprite Attributes
        self.spriteState = 0
        self.currentTime = 0
        self.hasFired = False

        #ParticleClass
        self.particle=Particle(True,pos,vel,maxVel,0,angle,radius,spriteKey,spriteDictionary,spriteFps,False,False,self.idObject)



    def recieve(self,other):
        self.maxVel=other.maxVel
        self.spriteState=other.spriteState
        self.currentTime=other.currentTime
        self.particle=other.particle



    def draw(self, canvas, cam,spriteDictionary):

        self.particle.draw(canvas, cam,spriteDictionary)

    def move(self,pos):
        self.particle.move(pos)


    def update(self):
        self.particle.update()
        self.currentTime = time.time()

        if self.spriteState==0:
            self.setCorrectAnimation()
        print(self.clickPosition)
        #CORRECT SPRITE ROW AND UPDATE FPS
        if self.hasFired and self.particle.spriteSheet.hasLooped:
            print("finished Firing")
            self.hasFired=False
            self.setCorrectAnimation()
        if self.particle.vel.getX()==0 and self.particle.vel.getY()==0 and not self.hasFired:
            self.particle.spriteSheet.currentColumn=1


    def setCorrectAnimation(self):
        print(self.clickPosition)
        x,y=self.particle.pos.copy().distanceToVector(self.clickPosition)
        print(x)
        print("called")
        print(self.hasFired)
        if y < 0:
            if self.hasFired:
                self.setSpriteState(6)
                print("fired")

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
        data = {'hasFired':self.hasFired,'idObject':self.idObject,'idClass':self.idClass,'pos': {'x':self.particle.pos.x,'y': self.particle.pos.y}, 'vel': {'x':self.particle.vel.x, 'y':self.particle.vel.y}, 'maxVel': self.maxVel,
                'angle': self.particle.angle, 'radius': self.particle.radius, 'spriteKey': self.particle.spriteKey,'currentTime':self.currentTime,
                'spriteFps': self.particle.spriteSheet.fps,'remove':self.remove,'updateSprite':self.particle.updateSprite}
        return json.dumps(data)
