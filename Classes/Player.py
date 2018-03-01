import json
class Player:
    def __init__(self, pos, vel, angle):
        self.angle = angle
        self.pos = pos
        self.vel = vel
        self.radius = 10
        self.id=4
    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, "White", "White")

    def bounce(self, normal):
        self.vel.reflect(normal)


    def update(self):
        self.pos.add(self.vel)

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)