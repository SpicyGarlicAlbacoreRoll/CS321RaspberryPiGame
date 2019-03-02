import sys, pygame, pymunk
import gameObject, physicsSim

pygame.init()
screenWidth = 600
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

timeStep = 50       #milliseconds
timeStepSec = timeStep * 0.001
gravity = 9.8       #meters per second^2
playerMass = 1      #kilograms
clock = pygame.time.Clock()

player = pygame.image.load('basicHeart.png')
player = pygame.transform.scale(player, (128, 128))
playerSpeed = 5

groundTile = pygame.image.load('sandTile00.png')
groundTile = pygame.transform.scale(groundTile, (128, 128))


background = pygame.image.load('placeholderBG00.png')
background = pygame.transform.scale(background, (600, 500))

screen.blit(background, (0,0))

tan = 255, 234, 191
white = 255, 255, 255
bgColor = tan


objects = []
for x in range(1):
    o = gameObject.Player(player, playerSpeed, screenWidth, screenHeight, gravity, playerMass, timeStepSec)
    objects.append(o)

for x in range(10):
    o = gameObject.EnvironmentObject(groundTile, 0, screenWidth, screenHeight)
    objects.append(0)

localPhysicsSim = physicsSim.PhysicsSim(objects, clock)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    localPhysicsSim.updatePhysicsSim(clock)

    for o in objects:
        screen.blit(background, o.pos)

    for o in objects:
        o.update()
        screen.blit(o.image, o.pos)

    localPhysicsSim.space.step(0.02)

    pygame.display.update()
    #pygame.time.delay(timeStep) #in milliseconds(?)
    clock.tick(50)