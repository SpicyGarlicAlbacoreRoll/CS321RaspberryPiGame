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
        self.position = Vec2D(position.getX(), position.getY())
        self.width = sprite[0]
        self.height = sprite[1]

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def update(self):
        self.physics()

    def physics(self):
        otherVec = Vec2D(2, 2)
        self.position.addVec(otherVec)


##########################################################
#              W O R L D  S P A C E                      #
#                   C L A S S                            #
##########################################################

class worldSpace:
    def __init__(self, gravity):
        self.g = gravity

    def update(self, colliderList):
        for obj in colliderList:
            if obj.isStatic == False:    #If the collider is from an enviroment obj, we ignore it
                for otherObj in colliderList:   #checks every gameobject's collider against the other


                #CHECK LEFT SIDE of OBJ vs RIGHT SIDE of other.
                    if (obj.position.getX() <= otherObj.position.getX() + otherObj.getWidth()
                    and obj.position.getX() > otherObj.position.getX()):                        
                        offset = (otherObj.position.getX() + otherObj.getWidth()) - obj.position.getX() + 1
                        obj.position.setX(obj.position.getX() + offset)
                
                    #CHECK BOTTOM of OBJ vs TOP of other.
                    # if (obj.position.getY() <= otherObj.position.getY() + otherObj.getHeight()
                    # and obj.position.getY() > otherObj.position.getY()):                        
                    #     offset = (otherObj.position.getX() + otherObj.getWidth()) - obj.position.getX() + 1
                    #     obj.position.setX(obj.position.getX() + offset)
                