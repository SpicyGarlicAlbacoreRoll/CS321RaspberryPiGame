import sys, pygame
import gameObject
import mathClass




pygame.init()
screenWidth = 600
screenHeight = 500
size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)

#For some physics stuff later
timeStep = 10   #milliseconds. Lower to increase play speed
timeStepSec = timeStep * 0.001
gravity = 9.8       #meters per second^2
playerMass = 1      #kilograms

player = pygame.image.load('basicHeart.png')
player = pygame.transform.scale(player, (128, 128))
playerSpeed = [1, 1]
playerPos = [200, 5]

ground = pygame.image.load('groundTile00.png')
ground = pygame.transform.scale(ground, (64, 64))
groundPos = [screenWidth-64, screenHeight - 64]

background = pygame.image.load('placeholderBG00.png')
background = pygame.transform.scale(background, (600, 500))

#draws background with our bg image
screen.blit(background, (0,0))

tan = 255, 234, 191
white = 255, 255, 255
bgColor = tan


objects = []        #The list of objects we're gonna create
colliders = []      #The list of colliders we're gonna make for each of them

#Initialize worldspace for physics collisions
worldSpace = mathClass.worldSpace(gravity)

#initialize player gameobject, add it to a list, 
o = gameObject.Player(player, playerSpeed, playerPos, screenWidth, screenHeight, gravity, playerMass, timeStepSec)
objects.append(o)
c = o.collider
colliders.append(c)

counter = 0
for g in range(10):
    g = gameObject.Environment(ground, 0.0, [groundPos[0] - counter * 64, groundPos[1]], screenWidth, screenHeight)
    objects.append(g)
    #and add its collider to another list
    cg = g.collider
    colliders.append(cg)
    counter += 1

#Pygame main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Check colliders against all other colliders
    worldSpace.update(colliders)

    #Draw background
    screen.blit(background, (0,0))

    #Update objects and draw them
    for o in objects:
        o.update()
        screen.blit(o.image, (o.position.getX(), o.position.getY()))
    # worldSpace.update(colliders)
    pygame.display.update()
    pygame.time.delay(timeStep) #in milliseconds(?)
    