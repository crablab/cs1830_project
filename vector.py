import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other) 

    def getP(self):
        return (self.x, self.y)

    def copy(self):
        return Vector(self.x, self.y)

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return self.copy().add(other);

    def negate(self):
        return self.multiply(-1)

    def __neg__(self):
        return self.copy().negate()

    def subtract(self, other):
        return self.add(-other)

    def __sub__(self, other):
        return self.copy().subtract(other)

    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def __mul__(self, k):
        return self.copy().multiply(k)

    def __rmul__(self, k):
        return self.copy().multiply(k)

    def divide(self, k):
        return self.multiply(1/k)

    def __truediv__(self, k):
        return self.copy().divide(k)

    def normalize(self):
        return self.divide(self.length())

    def getNormalized(self):
        return self.copy().normalize()

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def lengthSquared(self):
        return self.x**2 + self.y**2

    def reflect(self, normal):
        n = normal.copy()
        n.multiply( 2*self.dot(normal) )
        self.subtract(n)
        return self
