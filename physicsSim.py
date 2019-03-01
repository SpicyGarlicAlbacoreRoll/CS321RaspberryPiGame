#WORK IN PROGRESS
import pygame
import pymunk
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
        for x in range(len(gameObjs)):
            if isinstance(x, gameObject.Player):
                x.attachPhysicsBody(self.playerBody)
                x.createPhysicsPolyBox(self.playerBox)
                self.space.add(x.physicsBody, x.playerBox)
                self.bodies.append(x)

    def updatePhysicsSim(self, clock):
        self.clock = clock
        for x in range(len(self.bodies)):
            x.updatePhysics(clock)
        