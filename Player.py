
USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
#polygons
ParticleSize=2500
#Sprites:
SpriteSize=200
#CAMERA
CamMinDist=200
CAM_SENSITIVITY=5
class Player:
    def __init__(self, pos, vel, angle):
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.radius = 10

    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, "White", "White")

    def bounce(self, normal):
        self.vel.reflect(normal)

    def update(self):
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)
