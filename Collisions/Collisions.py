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

    def _doesCollide_CircleRectangle(self, circle, rectangle):

        dist = (circle.pos_vector - rectangle.pos_vector).length()
        if (dist > circle.radius + rectangle.radius_max):
            return False
        if (dist <= circle.radius + rectangle.radius_min):
            return True
        
        ## CHeck that is suppost to be //2

        v_list = [
            Vector(rectangle.width//2,rectangle.height//2),
            Vector(-rectangle.width//2,rectangle.height//2),
            Vector(-rectangle.width//2,-rectangle.height//2),
            Vector(rectangle.width//2,-rectangle.height//2)]
        for i in range(-1, len(v_list)-1):
            if (self._getDistPointLine(circle.pos_vector,(rectangle.pos_vector + v_list[i],rectangle.pos_vector + v_list[i+1])) < circle.radius):
                return True
        return False

    def _doesCollide_CircleLine(self, circle, line):

        return ((self._getDistPointLine(circle.pos_vector, (line.pos_vector_1, line.pos_vector_2))) <= circle.radius)

    def _doesCollide_RectangleCircle(self, rectangle, circle):

        return self._doesCollide_CircleRectangle(circle, rectangle)

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

    def _doesCollide_RectangleLine(self, rectangle, line):

        for point in [line.pos_vector_1, line.pos_vector_2]:
            if (self._isPointInRectangle(rectangle, point)):
                return True

        v_list = [
            Vector(rectangle.width//2,rectangle.height//2),
            Vector(-rectangle.width//2,rectangle.height//2),
            Vector(-rectangle.width//2,-rectangle.height//2),
            Vector(rectangle.width//2,-rectangle.height//2)]

        line_line = (line.pos_vector_1, line.pos_vector_2)
        for i in range(-1, len(v_list)-1):
            rect_line = (rectangle.pos_vector + v_list[i], rectangle.pos_vector + v_list[i+1])
            if (self._doLinesIntersect(rect_line, line_line)):
                return True

        return False

    def _doesCollide_LineCircle(self, line, circle):

        return self._doesCollide_CircleLine(circle, line)

    def _doesCollide_LineRectangle(self, line, rectangle):

        return self._doesCollide_RectangleLine(rectangle, line)

    def _doesCollide_LineLine(self, line_1, line_2):

        return self._doLinesIntersect(
            (line_1.pos_vector_1, line_1.pos_vector_2),
            (line_2.pos_vector_1, line_2.pos_vector_2))

    def _doCirclesIntersect(self, pos_vector_1, radius_1, pos_vector_2, radius_2):

        distance_points = (pos_vector_1 - pos_vector_2).length()
        distance_radius = radius_1 + radius_2
        return(distance_points <= distance_radius)

    def _doLinesIntersect(self, line_1, line_2):

        orien_1 = self._getPointOrientation(line_1[0], line_1[1], line_2[0])
        orien_2 = self._getPointOrientation(line_1[0], line_1[1], line_2[1])
        orien_3 = self._getPointOrientation(line_2[0], line_2[1], line_1[0])
        orien_4 = self._getPointOrientation(line_2[0], line_2[1], line_1[1])

        if (orien_1 != orien_2 and orien_3 != orien_4):
            return True

        if (orien_1 == 0 and onSegment(line_1[0], line_2[0], line_1[1])):
            return True
 
        if (orien_2 == 0 and onSegment(line_1[0], line_2[1], line_1[0])):
            return True
 
        if (orien_3 == 0 and onSegment(line_2[0], line_1[0], line_2[1])):
            return True
 
        if (orien_4 == 0 and onSegment(line_2[0], line_1[1], line_2[1])):
            return True

        return False

    def _getPointOrientation(self, p , q, r):
        #Used for calculating line collisions
        #0 --> p, q and r are colinear
        #1 --> Clockwise
        #2 --> Counterclockwise

        value = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

        if (value == 0):
            return 0

        return 1 if (value > 0) else 2

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
         
    def _isOnSegment(self, line, point):
        if (line[1].x <= max(line[0].x, point.x) and 
            line[1].x >= min(line[0].x, point.x) and
            line[1].y <= max(line[0].y, point.y) and
            line[1].y >= min(line[0].y, point.y)):
            return True
        return False

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
            "rectangle":_doesCollide_CircleRectangle,
            "line":_doesCollide_CircleLine
            },
        "rectangle":{
            "circle":_doesCollide_RectangleCircle,
            "rectangle":_doesCollide_RectangleRectangle,
            "line":_doesCollide_RectangleLine
            },
        "line":{
            "circle":_doesCollide_LineCircle,
            "rectangle":_doesCollide_LineRectangle,
            "line":_doesCollide_LineLine
        }}

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
        self.radius_min = min(self.width, self.height)

class CollisionLine(CollisionShape):
    def __init__(self, pos_vector_1, pos_vector_2):
        CollisionShape.__init__(self, "line")
        self.pos_vector_1 = pos_vector_1
        self.pos_vector_2 = pos_vector_2
    

a = CollisionRectangle(Vector(50,50), 10, 90)
b = CollisionRectangle(Vector(70,70), 5, 80)
c = CollisionCircle(Vector(70,70), 10)
d = CollisionLine(Vector(70,90),Vector(90,70))
e = CollisionLine(Vector(200,200),Vector(10,10))

"""
print(d.doesCollide(e))
print(e.doesCollide(d))
print(d.doesCollide(a))
print(d.doesCollide(b))
print(d.doesCollide(c))
"""






        
