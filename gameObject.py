import pygame
import mathClass

############################## GAMEOBJECT CLASS ##################################
class GameObject:
    def __init__(self, image, speed, position, screenWidth, screenHeight):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, 0)
        self.position = mathClass.Vec2D(position[0], position[1])
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.spriteWidth = self.image.get_size()[0]
        self.spriteHeight = self.image.get_size()[1]
        self.spriteCenter = [self.spriteWidth / 2, self.spriteHeight / 2]
        self.collider = mathClass.Collider(image, False, self.position, self.speed)
        
    #Placeholder
    def update(self):
        self.playAnim()

    #Placeholder for animation loop
    def playAnim(self):
        x = 1   #placeHolder

class Environment(GameObject):
    def __init__(self, image, speed, position, screenWidth, screenHeight):
        GameObject.__init__(self, image, speed, position, screenWidth, screenHeight)
        self.collider = mathClass.Collider(image, True, self.position, self.speed)

############################## PLAYER CLASS ##################################

class Player(GameObject):
    def __init__(self, image, speed, position, screenWidth, screenHeight, gravity, mass, timeStep):
        GameObject.__init__(self, image, speed, position, screenWidth, screenHeight)
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

    def update(self):
        GameObject.update(self)
        self.updatePhysics()
        self.collider.update(self.position)                 #Updates position of collider    
        self.playerController()                             #Reads player inputs


    #Old function, tracks cursor, wraps around screen
    def mouseFollow(self, pos):

        if pos[0] < self.screenWidth and pos[0] > 0:
            self.pos[0] = self.image.get_rect().move(pos)[0] - self.spriteCenter[0]
        if pos[1] < self.screenHeight and pos[1] > 0:
            self.pos[1] = self.image.get_rect().move(pos)[1] - self.spriteCenter[1]

    #Implements WASD controls to move player around screen.
    #Bounds checking for player is done here as well.
    def playerController(self):

        positionX = self.position.getX()
        positionY = self.position.getY()
        keys = pygame.key.get_pressed()

    #WASD CONTROLLER
        if(keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
        
        #VERTICAL
            if pygame.key.get_pressed()[pygame.K_w]:
                if positionY >= 0 - self.spriteCenter[1]:   
                    positionY -= self.speed #+ self.displacement
            if pygame.key.get_pressed()[pygame.K_s]:
                if positionY <= self.screenHeight - self.spriteCenter[1]:  
                    positionY += self.speed #self.displacement

        #HORIZONTAL
            if pygame.key.get_pressed()[pygame.K_a]:
                if positionX >= 0 - self.spriteCenter[0]:
                    positionX -= self.speed #+ self.displacement
            if pygame.key.get_pressed()[pygame.K_d]:
                if positionX <= self.screenWidth - self.spriteCenter[0]:
                    positionX += self.speed #+ self.displacement

            
            self.position.setX(positionX)
            self.position.setY(positionY)
            # self.collider.position.setX(positionX)
            # self.collider.position.setY(positionY)
            self.timeSinceKeyDown = 0
            print("objects: ", self.position.getX(), self.position.getY())   #For debugging player position vs collider position
            print("collider:", self.collider.position.getX(), self.collider.position.getY())              #(They should be the same)

        elif (self.timeSinceKeyDown < 3):
            self.timeSinceKeyDown += 1
        else:
            self.displacement = 0
            positionY += 9
            self.position.setY(positionY)
            self.velocity = self.initialVelocity
            

    def updatePlayerState(self):
        self.playerState = self.playerStates[0]

    #Updates the velocity over time with a constant acceleration
    def updatePhysics(self):
        self.velocity = 1 * self.timeStep + self.velocity
            #d = v[0]t + 0.5 * a * t^2

        self.displacement = self.velocity * 2 + 0.5 * 1 * self.timeStep**2
        # self.position.setX(5)
        # self.position.setY(50)