#WORK IN PROGRESS
import pygame
import pymunk
import pymunk.pygame_util
import gameObject

class PhysicsSim:
    def __init__(self, gameObjs, clock):
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.bodies = []
        self.playerBody = pymunk.Body(1, 1666)
        self.playerBox = pymunk.Poly.create_box(self.playerBody)
        self.clock = clock

    #iterate through array of gameobjects, create physics body for each player/env
        for x in gameObjs:
            if isinstance(x, gameObject.Player):
                x.attachPhysicsBody(self.playerBody)
                x.createPhysicsPolyBox(self.playerBox)
                self.space.add(x.physicsBody, x.physicsBox)
                self.bodies.append(x)

    def updatePhysicsSim(self, clock):
        self.clock = clock
        for x in self.bodies:
            #x.physicsBody.position.x += 500
            x.pos = x.physicsBody.position
            if x.pos[1] > 0:
                x.updatePhysics(self.clock, x.pos)
            #x.
        