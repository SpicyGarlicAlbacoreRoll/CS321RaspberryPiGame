import sys, pygame

pygame.init()
screenWidth = 600
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

player = pygame.image.load('basicHeart.png')
player = pygame.transform.scale(player, (128, 128))
background = pygame.image.load('placeholderBG00.png')
background = pygame.transform.scale(background, (600, 500))

screen.blit(background, (0,0))

tan = 255, 234, 191
white = 255, 255, 255
bgColor = tan



class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self, xspeed, yspeed):
        self.pos = self.pos.move(xspeed, yspeed)
        if self.pos.right > screenWidth:
            self.pos.left = 0
    def update(self):
        pos = pygame.mouse.get_pos()
        self.pos = self.image.get_rect().move(pos)
        if self.pos.right > screenWidth:
            self.pos.left = 0
            pygame.mouse.set_pos(self.pos.x, self.pos.y)


objects = []
for x in range(1):
    o = GameObject(player, x * 40, x)
    objects.append(o)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for o in objects:
            screen.blit(background, o.pos, o.pos)
    for o in objects:
        #o.move(1, 1)
        o.update()
        screen.blit(o.image, o.pos)

    #screen.fill(bgColor)
    #pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(50)
    