import json
import time
from Classes.Vector import Vector
class Player:
    def __init__(self, pos, vel, angle,idP):
        #id's
        self.id = 4
        self.idP = idP
        #non-vectors (attributes)
        self.maxVel=100
        self.angle = angle
        self.radius = 10  # multiply by 200
        #vectors
        self.pos = pos
        self.vel = vel
        self.nextPos=Vector(0,0)
        self.nextPosTime=0

        self.time=0

    def draw(self, canvas):

        canvas.draw_circle(self.pos.getP(), self.radius, 1, "White", "White")

    def bounce(self, normal):
        self.vel.reflect(normal)
    def move(self,pos):
        self.nextPos=pos
        self.timeTo()


        self.vel.negate()
    def transform(self,cam):
        self.width=cam.dim.getX()
        self.radius=self.radius * cam.dimCanv.copy().divideVector(cam.dim).getX()
        self.pos.subtract(cam.origin)
        ratio = cam.dimCanv.copy().divideVector(cam.dim)
        self.pos.multiplyVector(ratio)
        self.pos.add(cam.dimCanv.copy().divide(2))

    def update(self):
        if self.pos.copy().subtract(self.nextPos).dot(self.vel)>0:
            self.vel.multiply(0)
        x, y = self.pos.copy().distanceToVector(self.nextPos)
        dist = Vector(x, y)
        dist.negate()


        if self.nextPosTime-time.time()<0:
            self.pos=self.nextPos
        else:

            self.vel = dist.divide(self.nextPosTime - time.time())
            self.vel.multiply(time.time()-self.time)
            self.pos.add(self.vel)
        self.time=time.time()

    def turn(self, angle):
        self.angle+=angle

    def timeTo(self):
        self.nextPosTime=time.time()+self.pos.copy().distanceTo(self.nextPos)/self.maxVel


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)