import pygame


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

    def playAnim(self):
        x = 1   #placeHolder

############################## PLAYER CLASS ##################################

class Player(GameObject):
    def __init__(self, image, speed, screenWidth, screenHeight):
        GameObject.__init__(self, image, speed, screenWidth, screenHeight)
        self.playerStates = ["IDLE", "RUNNING", "JUMPING"]
        self.playerState = self.playerStates[0]

    def update(self):
        GameObject.update(self)
        self.playerController()
        #pos = pygame.mouse.get_pos()
        #self.mouseFollow(pos)

    def mouseFollow(self, pos):
        if pos[0] < self.screenWidth and pos[0] > 0:
            self.pos[0] = self.image.get_rect().move(pos)[0] - self.spriteCenter[0]
        if pos[1] < self.screenHeight and pos[1] > 0:
            self.pos[1] = self.image.get_rect().move(pos)[1] - self.spriteCenter[1]

    def playerController(self):
    #WASD CONTROLLER
        #VERTICAL
        if pygame.key.get_pressed()[pygame.K_w]:
            if self.pos[1] >= 0 - self.spriteCenter[1]:   
                self.pos[1] -= self.speed
        if pygame.key.get_pressed()[pygame.K_s]:
            if self.pos[1] <= self.screenHeight - self.spriteCenter[1]:  
                self.pos[1] += self.speed

        #HORIZONTAL
        if pygame.key.get_pressed()[pygame.K_a]:
            if self.pos[0] >= 0 - self.spriteCenter[0]:
                self.pos[0] -= self.speed
        if pygame.key.get_pressed()[pygame.K_d]:
            if self.pos[0] <= self.screenWidth - self.spriteCenter[0]:
                self.pos[0] += self.speed


    def updatePlayerState(self):
        self.playerState = self.playerStates[0]