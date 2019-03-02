import pygame
import pymunk
#from pygame.math import *

############################## GAMEOBJECT CLASS ##################################

class GameObject:
    def __init__(self, image, speed, screenWidth, screenHeight):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, 0)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.spriteWidth = self.image.get_size()[0]
        self.spriteHeight = self.image.get_size()[1]
        self.spriteCenter = [self.spriteWidth / 2, self.spriteHeight / 2]
    def update(self):
        self.playAnim()
        #self.pos = self.physicsBody.pos


    def playAnim(self):
        x = 1   #placeHolder


######################### PYMUNK PHYSICS FUNCTIONS ###########################
    
    def attachPhysicsBody(self, physBody):
        self.physicsBody = physBody
        self.physicsBody.position = 2, 2

    def createPhysicsPolyBox(self, physicsBox):
        self.physicsBox = physicsBox

    def updatePhysics(self, physicsClock, newPos):
        self.physicsClock = physicsClock
        self.pos = newPos





##############################################################################
############################## PLAYER CLASS ##################################
##############################################################################

class Player(GameObject):
    def __init__(self, image, speed, screenWidth, screenHeight, gravity, mass, timeStep):
        GameObject.__init__(self, image, speed, screenWidth, screenHeight)
        self.playerStates = ["IDLE", "RUNNING", "JUMPING"]
        self.playerState = self.playerStates[0]

#####INITIALIZE/ASSIGN PHYSICS VARIABLES#####    
            #v = a(t) + v[0]
            #d = v[0]t + 0.5 * a * t^2

        self.gravity = gravity
        self.velocity = speed       #will fix later and just remove speed
        self.initialVelocity = self.velocity
        self.force = gravity * mass
        self.timeStep = timeStep
        self.timeSinceKeyDown = 0
        self.displacement = 0

        #self.velocity = pygame.math

    def update(self):
        GameObject.update(self)
        #self.updatePhysicsTemp()
        #self.playerController()
        
    def mouseFollow(self, pos):
        if pos[0] < self.screenWidth and pos[0] > 0:
            self.pos[0] = self.image.get_rect().move(pos)[0] - self.spriteCenter[0]
        if pos[1] < self.screenHeight and pos[1] > 0:
            self.pos[1] = self.image.get_rect().move(pos)[1] - self.spriteCenter[1]

    def playerController(self):
    #WASD CONTROLLER
        #VERTICAL
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
            if pygame.key.get_pressed()[pygame.K_w]:
                if self.pos[1] >= 0 - self.spriteCenter[1]:   
                    self.pos[1] -= self.speed + self.displacement
            if pygame.key.get_pressed()[pygame.K_s]:
                if self.pos[1] <= self.screenHeight - self.spriteCenter[1]:  
                    self.pos[1] += self.speed + self.displacement

            #HORIZONTAL
            if pygame.key.get_pressed()[pygame.K_a]:
                if self.pos[0] >= 0 - self.spriteCenter[0]:
                    self.pos[0] -= self.speed + self.displacement
            if pygame.key.get_pressed()[pygame.K_d]:
                if self.pos[0] <= self.screenWidth - self.spriteCenter[0]:
                    self.pos[0] += self.speed + self.displacement
        
            self.timeSinceKeyDown = 0

        elif (self.timeSinceKeyDown < 3):
            self.timeSinceKeyDown += 1
        else:
            self.displacement = 0
            self.velocity = self.initialVelocity
            

    def updatePlayerState(self):
        self.playerState = self.playerStates[0]

    def updatePhysicsTemp(self):
        self.velocity = 1 * self.timeStep + self.velocity
            #d = v[0]t + 0.5 * a * t^2

        self.displacement = self.velocity + 0.5 * 1 * self.timeStep**2




##############################################################################
######################## ENVIRONMENT CLASS ###################################
##############################################################################

class EnvironmentObject(GameObject):
    def __init__(self, image, speed, screenWidth, screenHeight):
        GameObject.__init__(self, image, speed, screenWidth, screenHeight)
        
    