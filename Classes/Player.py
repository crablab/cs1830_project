import json
from Classes.Vector import Vector
class Player:
    def __init__(self, pos, vel, angle,idP):
        self.id = 4
        self.idP = idP
        self.maxVel=10
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.nextPos=Vector(0,0)
        self.radius = 2000  # multiply by 200
        self.width=0 #cam width.
    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius/self.width, 1, "White", "White")

    def bounce(self, normal):
        self.vel.reflect(normal)
    def move(self,pos):
        self.nextPos=pos
        self.vel=self.pos.copy().subtract(pos).normalize().multiply(self.maxVel)
        self.vel.negate()
    def transform(self,cam):


        self.width=cam.dim.getX()
        #get Distance

        dist=self.pos.copy()
        dist.subtract(cam.origin)

        #get ratio
        ratio=dist.divideVector(cam.dim.copy().divide(2))

        #multiply ration on real screen
        self.pos=ratio.multiplyVector(cam.dimCanv.copy().divide(2))
        self.pos.add(cam.dimCanv.copy().divide(2))

    def update(self):

        if self.pos.copy().subtract(self.nextPos).dot(self.vel)>0:
            self.vel.multiply(0)
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)