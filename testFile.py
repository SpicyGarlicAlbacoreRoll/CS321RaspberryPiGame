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
playerSpeed = 5

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
o = gameObject.Player(player, playerSpeed, screenWidth, screenHeight, gravity, playerMass, timeStepSec)
objects.append(o)

#and add its collider to another list
c = o.collider
colliders.append(c)


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

    pygame.display.update()
    pygame.time.delay(timeStep) #in milliseconds(?)
    