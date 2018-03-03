from vector import Vector
import math
"""
Assume that shape characyeristics dont change, but pos does
"""

class CollisionHandler:
    def doesCollide(self, object_1, object_2):
        return self.collision_dict[object_1.shape_type][object_2.shape_type](self, object_1, object_2)
    
    def _doesCollide_CircleCircle(self, circle_1, circle_2):
        return self._doCirclesIntersect(
            circle_1.pos_vector,
            circle_1.radius,
            circle_2.pos_vector,
            circle_2.radius)

    def _doCirclesIntersect(self, pos_vector_1, radius_1,
                             pos_vector_2, radius_2):
        distance_points = (pos_vector_1 - pos_vector_2).length()
        distance_radius = radius_1 + radius_2
        return(distance_points <= distance_radius)

    def _doesCollide_RectangleRectangle(self, rectangle_1, rectangle_2):
        if ((rectangle_1.pos_vector - rectangle_2.pos_vector).length() > rectangle_1.radius_max + rectangle_2.radius_max):
            return False

        for i in [-1,1]:
            for j in [-1,1]:
                if (self._isPointInRectangle(rectangle_1, rectangle_2.pos_vector + Vector((rectangle_2.width//2)*i + rectangle_2.height//2)*j)):
                    return True
                if (self._isPointInRectangle(rectangle_2, rectangle_1.pos_vector + Vector((rectangle_1.width//2)*i + rectangle_1.height//2)*j)):
                    return True

        return False

    def _isPointInRectangle(self, rectange, point_vector):
        if (rectange.pos_vector.x + rectange.width//2 < point_vector.x):
            return False
        if (rectange.pos_vector.x - rectange.width//2 > point_vector.x):
            return False
        if (rectange.pos_vector.y + rectange.height//2 < point_vector.y):
            return False
        if (rectange.pos_vector.y - rectange.height//2 > point_vector.y):
            return False
        return True

    def _doesCollide_CircleRectangle(self, circle, rectangle):
        dist = (circle.pos_vector - rectangle.pos_vector).length()
        if (dist > circle.radius + rectangle.radius_max):
            return False
        if (dist <= circle.radius + rectangle.radius_min):
            return True
        
        v_list = [
            Vector(rectangle.width,rectangle.height),
            Vector(-rectangle.width,rectangle.height),
            Vector(-rectangle.width,-rectangle.height),
            Vector(rectangle.width,-rectangle.height)]
        for i in range(-1, len(v_list)-1):
            if (self._getDistPointLine(circle.pos_vector,(rectangle.pos_vector + v_list[i],rectangle.pos_vector + v_list[i+1])) < circle.radius):
                return True
        return False

    def _doesCollide_RectangleCircle(self, rectangle, circle):
        return self._doesCollide_CircleRectangle(circle, rectangle)
            
    def _getDistPointLine(self, point_vector, line_vector_pair):
        #https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment
        A = point_vector.x - line_vector_pair[0].x
        B = point_vector.y - line_vector_pair[0].y
        C = line_vector_pair[1].x - line_vector_pair[0].x
        D = line_vector_pair[1].y - line_vector_pair[0].y

        dot = A * C + B * D
        len_sq = C * C + D * D
        param = -1
        if (len_sq != 0):#in case of 0 length line
            param = dot / len_sq

        if (param < 0):
            xx = line_vector_pair[0].x
            yy = line_vector_pair[0].y
        elif (param >1):
            xx = line_vector_pair[1].x
            yy = line_vector_pair[1].y
        else:
            xx = line_vector_pair[0].x + param * C
            yy = line_vector_pair[0].y + param * D

        #can put in form of vector class
        dx = point_vector.x - xx
        dy = point_vector.y - yy
        return math.sqrt(dx * dx + dy * dy);
        

    collision_dict = {
        "circle":{
            "circle":_doesCollide_CircleCircle,
            "rectangle":_doesCollide_CircleRectangle
            },
        "rectangle":{
            "circle":_doesCollide_RectangleCircle,
            "rectangle":_doesCollide_RectangleRectangle
            }
        }

class CollisionShape:
    collision_handler = CollisionHandler()
    
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def doesCollide(self, other):
        return  self.collision_handler.doesCollide(self, other)

class CollisionCircle(CollisionShape):
    def __init__(self, pos_vector, radius):
        CollisionShape.__init__(self, "circle")
        self.pos_vector = pos_vector
        self.radius = radius

class CollisionRectangle(CollisionShape):
    def __init__(self, pos_vector, width, height):
        CollisionShape.__init__(self, "rectangle")
        self.pos_vector = pos_vector
        self.width = width
        self.height = height
        self.radius_max = math.sqrt(self.width**2 + self.height**2)
        if (self.width < self.height):
            self.radius_min = self.width
        else:
            self.radius_min = self.height

##a = CollisionRectangle(Vector(50,50), 10, 90)
##b = CollisionRectangle(Vector(70,70), 5, 80)
##c = CollisionCircle(Vector(70,70), 10)
##print(a.doesCollide(b))
##print(a.doesCollide(c))
##print(b.doesCollide(c))








        
