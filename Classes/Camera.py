from Classes.Vector import Vector
from Classes.Settings import CAM_MIN_DIST,CAM_ZOOM_SENSITIVITY,CAM_MOVE_SENSITIVITY,CANVAS_HEIGHT,CANVAS_WIDTH
class Camera:
    def __init__(self, origin, dim):
        self.origin = origin
        self.dim = dim
        self.dimCanv=Vector(CANVAS_WIDTH,CANVAS_HEIGHT)
        self.zoomIn=False
        self.zoomOut=False
        self.moveLeft=False
        self.moveRight=False
        self.moveUp=False
        self.moveDown=False
        self.idClass=1

    def move(self):
        if self.moveUp==True:
            self.origin.add(Vector(0,-CAM_MOVE_SENSITIVITY))
        if self.moveDown==True:
            self.origin.add(Vector(0,CAM_MOVE_SENSITIVITY))

        if self.moveLeft == True:
            self.origin.add(Vector(-CAM_MOVE_SENSITIVITY,0))
        if self.moveRight == True:
            self.origin.add(Vector(CAM_MOVE_SENSITIVITY,0))


    def zoom(self):
        if self.zoomOut == True:

            self.dim.add(self.dim.copy().multiply(CAM_ZOOM_SENSITIVITY))

        if self.zoomIn == True and self.dim.x>CAM_MIN_DIST and self.dim.y>CAM_MIN_DIST:

            self.dim.add(self.dim.copy().multiply(-CAM_ZOOM_SENSITIVITY))

    def ratioToCam(self):
        return(self.dimCanv.copy().divideVector(self.dim).getX())

    def ratioToCanv(self):
        return (self.dim.copy().divideVector(self.dimCanv).getX())

    def get(self):
        return(self.origin, self.dim.x)
