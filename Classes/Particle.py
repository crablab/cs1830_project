
class Particle:
    def __init__(self, pos, vel, angle,radius):
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.radius = radius

    def draw(self, canvas,width):
        canvas.draw_circle(self.pos.getP(), self.radius/width, 1, "Pink", "Pink")

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
        #get Distance

        dist=self.pos.copy()
        dist.subtract(cam.origin)

        #get ratio
        ratio=dist.divideVector(cam.dim.copy().divide(2))

        #multiply ration on real screen
        self.pos=ratio.multiplyVector(cam.dimCanv.copy().divide(2))
        self.pos.add(cam.dimCanv.copy().divide(2))


