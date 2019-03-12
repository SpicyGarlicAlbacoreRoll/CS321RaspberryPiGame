import pygame

##########################################################
#                  2-D  V E C T O R                      #
#                     C L A S S                          #
##########################################################
class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

###########################
# BASIC MATH OPERATIONS
###########################

    def add(self, x, y):
        self.x += x
        self.y += y
    
    def addVec(self, otherVector):
        self.setX(otherVector.getX() + self.getX())
        self.setY(otherVector.getY() + self.getY()) 

###########################
#    GETTERS & SETTERS
###########################
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

##########################################################
#           P H Y S I C S  C O L L I D E R               #
#                     C L A S S                          #
##########################################################

class Collider:
    def __init__(self, sprite, isStatic, position):
        self.g = 9.8                #gravity
        self.isStatic = isStatic
        self.position = Vec2D(0, 0)

    def update(self):
        self.physics()

    def physics(self):
        otherVec = Vec2D(2, 2)

        self.position.addVec(otherVec)
