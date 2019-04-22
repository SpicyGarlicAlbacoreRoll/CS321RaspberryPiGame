import pygame
import mathClass

############################## GAMEOBJECT CLASS ##################################
class GameObject:
    def __init__(self, image, speed, position, screenWidth, screenHeight):
        self.speed = speed
        self.image = image
        # self.pos = image.get_rect().move(0, 0)
        self.position = mathClass.Vec2D(position[0], position[1])
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.spriteWidth = self.image.get_width()
        self.spriteHeight = self.image.get_height()
        
        self.spriteCenter = [self.spriteWidth / 2, self.spriteHeight / 2]

        
    #Placeholder
    def update(self):
        self.playAnim()
        

    #Placeholder for animation loop
    def playAnim(self):
        x = 1   #placeHolder

class Environment(GameObject):
    def __init__(self, image, speed, position, screenWidth, screenHeight):
        GameObject.__init__(self, image, speed, position, screenWidth, screenHeight)
        self.collider = mathClass.Collider(self.image, True, self.position, self.speed)

    def update(self):
        x =1
        # self.position.setX(self.position.getX() + 1)
        

            # print("objects: ", self.position.getX(), self.position.getY())   #For debugging player position vs collider position
            # print("collider:", self.collider.position.getX(), self.collider.position.getY())              #(They should be the same)
############################## PLAYER CLASS ##################################

class Player(GameObject):
    def __init__(self, image, speed, position, screenWidth, screenHeight, gravity, mass, timeStep):
        GameObject.__init__(self, image, speed, position, screenWidth, screenHeight)
        self.collider = mathClass.Collider(self.image, False, self.position, self.speed)
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
        self.displacement = [0, 0]

    def update(self):
        GameObject.update(self)      
        self.playerController()                             #Reads player inputs
        self.position = self.collider.position
        # print(self.position.getX(), self.position.getY())
        # print(self.speed)


    #Old function, tracks cursor, wraps around screen
    # def mouseFollow(self, pos):

    #     if pos[0] < self.screenWidth and pos[0] > 0:
    #         self.pos[0] = self.image.get_rect().move(pos)[0] - self.spriteCenter[0]
    #     if pos[1] < self.screenHeight and pos[1] > 0:
    #         self.pos[1] = self.image.get_rect().move(pos)[1] - self.spriteCenter[1]

    #Implements WASD controls to move player around screen.
    #Bounds checking for player is done here as well.
    def playerController(self):

        positionX = self.collider.position.getX()
        positionY = self.collider.position.getY()
        keys = pygame.key.get_pressed()

    #WASD CONTROLLER
        if(keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_SPACE]):
        
        # #VERTICAL
        #     if pygame.key.get_pressed()[pygame.K_w]:
        #         if positionY >= 0 - self.spriteCenter[1]:
        #             # self.speed[1] = -1    
        #             positionY -= self.speed[1] #+ self.displacement
        #     if pygame.key.get_pressed()[pygame.K_s]:
        #         if positionY <= self.screenHeight - self.spriteCenter[1]:
        #             # self.speed[1] = 1  
        #             positionY += self.speed[1] #self.displacement

        #HORIZONTAL
            if pygame.key.get_pressed()[pygame.K_a]:
                if positionX >= 0:
                    x = 1
                    # self.speed[0] = -1
                    positionX -= self.speed[0]*6 #+ self.displacement
            if pygame.key.get_pressed()[pygame.K_d]:
                if positionX <= self.screenWidth - self.spriteWidth:
                    y = 1
                    # self.speed[0] = 1
                    positionX += self.speed[0]*6 #+ self.displacement
            if self.collider.isGrounded == True:
                if keys[pygame.K_SPACE]:
                    self.collider.isGrounded = False
                    self.speed[1] = -2.5
                    self.position.setY(positionY + self.speed[1])
                    print("JUMPING")

            # print(self.collider.position.getX(), self.collider.position.getY())
            self.timeSinceKeyDown = 0


        elif (self.timeSinceKeyDown < 3):
            self.timeSinceKeyDown += 1
        if self.speed[1] < 0 and self.collider.isGrounded == False:
            self.speed[1] +=  self.gravity * self.timeStep
        # self.position.setY(positionY)
        self.position.setX(positionX)
        # self.position.setY(positionY)
        # self.collider.update(self.position, self.speed)

    def updatePlayerState(self):
        self.playerState = self.playerStates[0]

    #Updates the velocity over time with a constant acceleration
    def updatePhysics(self):
        self.velocity[0] = 1 * self.timeStep + self.velocity[0]
        self.velocity[1] = 1 * self.timeStep + self.velocity[1]      
            #d = v[0]t + 0.5 * a * t^2

        self.displacement[0] = self.velocity[0] * 2 + 0.5 * 1 * self.timeStep**2
        self.displacement[1] = self.velocity[1] * 2 + 0.5 * 1 * self.timeStep**2
        # self.position.setX(5)
        # self.position.setY(50)