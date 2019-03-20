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
        self.width = sprite.get_rect().x
        self.height = sprite.get_rect().y

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def update(self, position):
        self.physics(position)

    def physics(self, position):
        self.position.setX(position.getX())
        self.position.setY(position.getY())
        # otherVec = Vec2D(2, 2)
        # self.position.addVec(otherVec)


##########################################################
#              W O R L D  S P A C E                      #
#                   C L A S S                            #
##########################################################

class worldSpace:
    def __init__(self, gravity):
        self.g = gravity

    def update(self, colliderList):
        for obj in colliderList:
            i = 0
            if obj.isStatic == False:           #If the collider is from an enviroment obj, we ignore it
                j = 0
                for otherObj in colliderList:   #checks every gameobject's collider against the other
                    if i != j:                  #Skips objects comparing to self
                    
                    #Variables written this way cause it's a lot easier to 
                    #conceptualize intersections between objects
                    #OBJECT MIDPOINTS
                        objMidPointX = obj.position.getX() + obj.getWidth() / 2
                        objMidPointY = obj.position.getY() + obj.getHeight() / 2
                        otherObjMidPointX = otherObj.position.getX() + otherObj.getWidth() / 2
                        otherObjMidPointY = otherObj.position.getY() + otherObj.getHeight() / 2

                    #SIDES OF OBJECTS (LEFT, RIGHT, BOTTOM, TOP)
                        objLeftSide     =   obj.position.getX()
                        objRightSide    =   objLeftSide + obj.getWidth()
                        objBottom       =   obj.position.getY()
                        objTop          =   objBottom + obj.getHeight()

                        otherObjLeftSide    =   otherObj.position.getX()
                        otherObjRightSide   =   otherObjLeftSide + otherObj.getWidth()
                        otherObjBottom      =   otherObj.position.getY()
                        otherObjTop         =   otherObjBottom + otherObj.getHeight()

                    #Debugging code
                        # print("Midpoint Object: ", objMidPointX)
                        # print("Midpoint otherObject: ", otherObjMidPointX)
                        
                    # X-AXIS INTERSECTION CHECK
                        if((objTop > otherObjBottom and objMidPointY < otherObjMidPointY)   #Top overlaps bottom
                        or (objBottom < otherObjTop and objMidPointY > otherObjMidPointY)): #Bottom overlaps top
                            
                            if (objLeftSide < otherObjRightSide        #Left side is to left of other objects right side
                            and objMidPointX >= otherObjMidPointX      #Object midpoint is greater than other object midpoint
                            and objBottom < otherObjTop):                            
                                offset = otherObjRightSide - objLeftSide
                                obj.position.setX(obj.position.getX() + offset)
                                print("PUSH RIGHT")
                                
                            elif(objRightSide > otherObjLeftSide
                            and objMidPointX < otherObjMidPointX):
                                offset = objRightSide - otherObjLeftSide  
                                obj.position.setX(obj.position.getX() - offset)
                                print("PUSH LEFT")

                    # Y-AXIS INTERSECTION CHECK
                        if((objRightSide > otherObjLeftSide and objMidPointX < otherObjMidPointX)   #Right overlaps Left
                        or (objLeftSide < otherObjRightSide and objMidPointX > otherObjMidPointX)): #Left overlaps Right
                            
                            if (objBottom < otherObjTop             #Bottom of object coord is less than height
                            and objMidPointY >= otherObjMidPointY):   #Object midpoint is greater than other object midpoint
                                offset = otherObjTop - objBottom
                                obj.position.setY(objBottom + offset)
                                print("PUSH UP")
                                
                            elif(objTop > otherObjBottom
                            and objMidPointY < otherObjMidPointY):
                                offset = objTop - otherObjBottom  
                                obj.position.setY(objBottom - offset)
                                print("PUSH DOWN")                        
                    j += 1
                i += 1
