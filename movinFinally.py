import sys, pygame
import gameObject

pygame.init()
screenWidth = 600
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

player = pygame.image.load('basicHeart.png')
player = pygame.transform.scale(player, (128, 128))
playerSpeed = 20

background = pygame.image.load('placeholderBG00.png')
background = pygame.transform.scale(background, (600, 500))

screen.blit(background, (0,0))

tan = 255, 234, 191
white = 255, 255, 255
bgColor = tan


objects = []
for x in range(1):
    o = gameObject.Player(player, playerSpeed, screenWidth, screenHeight)
    objects.append(o)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for o in objects:
        screen.blit(background, o.pos, o.pos)

    for o in objects:
        o.update()
        screen.blit(o.image, o.pos)

    pygame.display.update()
    pygame.time.delay(50)
    