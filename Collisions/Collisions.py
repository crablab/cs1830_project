from Classes.Vector import Vector

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

    def _doesCollide_CirclePolygon(self, circle, polygon):
        if not self._doCirclesIntersect(
                polygon.pos_vector,
                polygon.radius_max,
                circle.pos_vector,
                circle.radius):
            return False
        if self._doCirclesIntersect(
                polygon.pos_vector,
                polygon.radius_min,
                circle.pos_vector,
                circle.radius):
            return True

##        for (i = 0; i < polygon.numEdges; ++i) {
##            if (Distance(circle.center, polygon.edge) < circle.radius) {
##                return true;
##        return false;

##          float minimum_distance(vec2 v, vec2 w, vec2 p) {
##              // Return minimum distance between line segment vw and point p
##              const float l2 = length_squared(v, w);  // i.e. |w-v|^2 -  avoid a sqrt
##              if (l2 == 0.0) return distance(p, v);   // v == w case
##              // Consider the line extending the segment, parameterized as v + t (w - v).
##              // We find projection of point p onto the line. 
##              // It falls where t = [(p-v) . (w-v)] / |w-v|^2
##              // We clamp t from [0,1] to handle points outside the segment vw.
##              const float t = max(0, min(1, dot(p - v, w - v) / l2));
##              const vec2 projection = v + t * (w - v);  // Projection falls on the segment
##              return distance(p, projection);
##            }
        
        for i in range(-1,len(polygon_1.vector_array)-1):
            if (self._getMinimumDistLineCircle((polygon.vector_array[i], polygon.vector_array[i+1]), circle.pos_vector) < circle.radius):
                return True
        return False

    def _getMinimumDistLineCircle(self, line_vector_pair, circle_pos_vector):
        length_squared = (line_vector_pair[0] - line_vector_pair[1]).length()**2
        if (length_squared == 0.0):
            return (line_vector_pair[0] - circle_pos_vector).length()
        t = max(0,min(1,(circle_pos_vector - line_vector_pair[0]).dot(line_vector_pair[1] - line_vector_pair[0])/length_squared))
        projection = line_vector_pair[0] + t * (line_vector_pair[1] - line_vector_pair[0])
        return (circle_pos_vector - projection).length()

    def _doesCollide_PolygonCircle(self, polygon, circle):
        return self._doesCollide_CirclePolygon(circle, polygon)

    def _doesCollide_PolygonPolygon(self, polygon_1, polygon_2):
        ##will need optimisation
        
        if not self._doCirclesIntersect(
                polygon_1.pos_vector,
                polygon_1.radius_max,
                polygon_2.pos_vector,
                polygon_2.radius_max):
            return False
        if self._doCirclesIntersect(
                polygon_1.pos_vector,
                polygon_1.radius_min,
                polygon_2.pos_vector,
                polygon_2.radius_min):
            return True
        
        for i in range(-1,len(polygon_1.vector_array)-1):
            for j in range(-1,len(polygon_2.vector_array)-1):
                if self._doEdgesIntersect(
                        polygon_1.vector_array[i],
                        polygon_1.vector_array[i+1],
                        polygon_2.vector_array[i],
                        polygon_2.vector_array[i+1]):
                    return True
        return False



    def _determinant(vector_1, vector_2):
        ##Maybe put in vector class
        return vec1.x * vec2.y - vec1.y * vec2.x;
    
    def _doEdgesIntersect(self, a, b, c, d):
        """
        edge_1 = a -> b
        edge_2 = c -> d
        """
        det = _determinant(b - a, c - d)
        t = determinant(c - a, c - d) / det
        u = determinant(b - a, c - a) / det
        return not ((t < 0) or (u < 0) or (t > 1) or (u > 1))

    collision_dict = {
        "circle":{
            "circle":_doesCollide_CircleCircle,
            "polygon":_doesCollide_CirclePolygon
            },
        "polygon":{
            "circle":_doesCollide_PolygonCircle,
            "polygon":_doesCollide_PolygonPolygon
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

class CollisionPolygon(CollisionShape):
    def __init__(self, pos_vector, relative_point_vector_array):
        CollisionShape.__init__(self, "polygon")
        
        self.pos_vector = pos_vector
        self.vector_array = relative_point_vector_array

        self.radius_min = (self.pos_vector - self.vector_array[0]).length()
        self.radius_max = self.radius_min

        for i in range(1,len(self.vector_array)):
            radius = (self.pos_vector - self.vector_array[i]).length()
            if (radius > self.radius_max):
                self.radius_max = radius
            elif (radius < self.radius_min):
                self.radius_min = radius

a = CollisionPolygon(Vector(50,50), [Vector(-10,-10),Vector(10,-10),Vector(10,10),Vector(-10,10)])
b = CollisionPolygon(Vector(55,55), [Vector(-10,-10),Vector(10,-10),Vector(10,10),Vector(-10,10)])
c = CollisionCircle(Vector(30,30), 50)
print(a.doesCollide(c))







        
