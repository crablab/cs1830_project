import json
from Classes.Vector import Vector
class Player:
    def __init__(self, pos, vel, angle,idP):
        #id's
        self.id = 4
        self.idP = idP
        #non-vectors (attributes)
        self.maxVel=10
        self.angle = angle
        self.radius = 250  # multiply by 200
        self.width = 0  # cam width.
        #vectors
        self.pos = pos
        self.vel = vel
        self.nextPos=Vector(0,0)

    def draw(self, canvas,cam):
        print(self.width)
        canvas.draw_circle(self.pos.getP(), self.radius, 1, "White", "White")

    def bounce(self, normal):
        self.vel.reflect(normal)
    def move(self,pos):
        self.nextPos=pos
        self.vel=self.pos.copy().subtract(pos).normalize().multiply(self.maxVel)
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
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)