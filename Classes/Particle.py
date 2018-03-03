import json
class Particle:
    def __init__(self, pos, vel, angle, radius):
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.radius = radius

        self.id=3
        self.time=0
    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, "Pink", "Pink")

    def bounce(self, normal):
        self.vel.reflect(normal)

    def update(self):
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)

    def copy(self):
        p=Particle(self.pos,self.vel,self.angle,self.radius)
        return(p)

    def transform(self,cam):
        self.width = cam.dim.getX()
        self.radius = self.radius * cam.dimCanv.copy().divideVector(cam.dim).getX()
        self.pos.subtract(cam.origin)
        ratio = cam.dimCanv.copy().divideVector(cam.dim)
        self.pos.multiplyVector(ratio)
        self.pos.add(cam.dimCanv.copy().divide(2))

    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)

