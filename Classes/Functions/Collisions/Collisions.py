from Classes.Base.Vector import Vector
import math


def doCirclesIntersect(pos1,radius1, pos2,radius2):
    distance_points = (pos1.copy().subtract(pos2)).length()
    distance_radius = radius1 + radius2
    return (distance_points <= distance_radius)

def isCircleInRect(posC,radius,posR,dim):
    distX=posC.getX()-posR.getX()
    if distX<0:
        distX*=-1
    distY = posC.getY() - posR.getY()
    if distY < 0:
        distY*= -1
    if distY < radius + dim.getY() and distX<radius+dim.getX():
        return True
    return False

def isPointInRect(point,rectOrigin,rectDim):
    xIn=point.getX()>rectOrigin.getX()-rectDim.getX() and point.getX()<rectOrigin.getX()+rectDim.getX()
    yIn=point.getY()>rectOrigin.getY()-rectDim.getY() and point.getY()<rectOrigin.getY()+rectDim.getY()
    print(xIn and yIn)
    return xIn and yIn







        
