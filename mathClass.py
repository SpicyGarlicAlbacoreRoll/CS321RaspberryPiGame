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
    def __init__(self, sprite, isStatic, position, velocity):
        self.g = 9.8                #gravity
        self.isStatic = isStatic
        self.position = Vec2D(position.getX(), position.getY())
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.speed = velocity
        self.isGrounded = False

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def update(self, position, speed):
        self.physics(position, speed)

    def physics(self, position, speed):
        self.position.setX(position.getX())
        self.position.setY(position.getY())
        self.speed = speed
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
        i = 0
        for obj in colliderList:
            if obj.isStatic == False:           #If the collider is from an enviroment obj, we ignore it
                j = 0
                for otherObj in colliderList:   #checks every gameobject's collider against the other
                    if obj != otherObj:                  #Skips objects comparing to self
                    
                    #Variables written this way cause it's a lot easier to 

                        objSpeedX = obj.speed[0]
                        objSpeedY = obj.speed[1]
                        
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
                        

                        if((objRightSide > otherObjLeftSide and
                        objRightSide < otherObjRightSide) and
                        ((objTop + objSpeedY > otherObjTop and      #top doesn't overlap other's top
                        objBottom + objSpeedY < otherObjTop) or     #bottom overlaps other's top
                        (objTop + objSpeedY > otherObjBottom and    #top overlap other's bottom
                        objBottom + objSpeedY < otherObjBottom)        #bottom doesn't overlap other's bottom
                        )):
                            # objSpeedY *= -1
                       
                            print("Update physics")
                            if obj.isGrounded == False:
                                obj.isGrounded = True
                                print("LANDED")
                            # obj.speed[1] = 0
                            print("Colliding: top" , j)
                            # obj.position.setY(obj.position.getY())
                        elif(objBottom < 0 or objTop > 500):
                            # objSpeedY *= -1
                            print("Colliding: WALL")
                        elif obj.isGrounded == False:
                            print("FALLING")
                            obj.position.setY(obj.position.getY())

                        if obj.isGrounded == False and (((objRightSide + objSpeedX > otherObjLeftSide and        #right side overlap other's left
                        objLeftSide + objSpeedX < otherObjLeftSide) or             #left side doesn't overlap other's left
                        (objLeftSide + objSpeedX < otherObjRightSide and            #left side overlaps other's right
                        objRightSide + objSpeedX > otherObjRightSide) and          #right side doesn't overlap other's left
                        ((objTop > otherObjBottom and
                        objBottom < otherObjTop) or
                        objBottom > otherObjBottom and
                        objTop > otherObjTop))):
                            obj.position.setX(obj.position.getX() - objSpeedX)

                        elif(objLeftSide < 0 or objRightSide > 600):

                            print("Colliding: WALL")


                    else:
                        j += 1
            i += 1
