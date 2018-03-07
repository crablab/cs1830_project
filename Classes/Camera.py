from Classes.Vector import Vector
from Classes.Settings import CAM_MIN_DIST,CAM_ZOOM_SENSITIVITY,CAM_MOVE_SENSITIVITY,CANVAS_HEIGHT,CANVAS_WIDTH
import json
import uuid
import time
class Camera:
    def __init__(self, origin, dim):
        self.idClass = 1
        self.idObject = uuid.uuid4()

        self.origin = origin
        self.dim = dim
        self.dimCanv=Vector(CANVAS_WIDTH,CANVAS_HEIGHT)
        self.zoomIn=False
        self.zoomOut=False
        self.moveLeft=False
        self.moveRight=False
        self.moveUp=False
        self.moveDown=False

        self.currentTime=time.time()


    def move(self):
        self.currentTime=time.time()
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
            if self.dim.x < 600 or self.dim.y < 600:
                pass
            else:
                self.dim.add(self.dim.copy().multiply(-CAM_ZOOM_SENSITIVITY))

    def ratioToCam(self):
        return(self.dimCanv.copy().divideVector(self.dim).getX())

    def ratioToCanv(self):
        return (self.dim.copy().divideVector(self.dimCanv).getX())

    def get(self):
        return(self.origin, self.dim.x)

    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
