import json
import time
import os
import json
from Classes.SpriteSheet import SpriteSheet
from Classes.Vector import Vector
class Particle:

    def __init__(self, pos, vel, angle, dim,radius,spriteKey,maxVel,maxRange,removeOnVelocity0,removeOnAnimationLoop):
        self.pos = pos
        self.vel = vel
        self.nextPos = pos
        self.nextPosTime = 0
        self.maxVel=maxVel

        self.maxRange=maxRange
        self.angle = angle
        self.dim=dim
        self.radius=radius
        self.spriteKey=spriteKey
        self.sprite=SpriteSheet(self.pos,spriteKey)
        self.removeOnAnimationLoop=removeOnAnimationLoop
        self.removeOnVelocity0=removeOnVelocity0

        self.idClass=2
        self.currentTime=time.time()

    def draw(self, canvas, cam,spriteDictionary):
        # ratio = cam.dimCanv.copy().divideVector(cam.dim)
        # self.radius*=ratio.getX()
        # canvas.draw_circle(self.pos.getP(), self.radius, 1, 'White')
        self.sprite.draw(canvas, cam, self.pos,self.angle,spriteDictionary)

    def bounce(self, normal):
        self.vel.reflect(normal)

    def moveRange(self,pos):
        dist = self.pos.copy().subtract(pos)

        dist.negate()
        if dist.length()!=0:
            dist.normalize().multiply(self.maxRange)

        self.nextPos = self.pos.copy().add(dist)

        self.timeTo(self.maxVel)
        self.vel.negate()
    def move(self, pos):
        self.nextPos = pos
        self.timeTo(self.maxVel)
        self.vel.negate()

    def update(self):
        if self.pos.copy().subtract(self.nextPos).dot(self.vel) > 0:
            self.vel.multiply(0)
        if self.pos!=self.nextPos:
            x, y = self.pos.copy().distanceToVector(self.nextPos)
            dist = Vector(x, y)
            dist.negate()

            if self.nextPosTime - time.time() <= 0:
                self.pos = self.nextPos
            else:
                self.vel = dist.divide(self.nextPosTime - time.time())
                self.vel.multiply(time.time() - self.currentTime)
                self.pos.add(self.vel)

            self.currentTime = time.time()
            self.pos.add(self.vel.copy().multiply(time.time()-self.currentTime))
        self.currentTime=time.time()

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)

    def copy(self):
        p=Particle(self.pos,self.vel,self.angle,self.dim,self.radius,self.spriteKey,self.maxVel,self.maxRange,self.removeOnVelocity0,self.removeOnAnimationLoop,)
        return(p)

    def timeTo(self,maxVel):
        self.nextPosTime = time.time() + self.pos.copy().distanceTo(self.nextPos) / maxVel

    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)

