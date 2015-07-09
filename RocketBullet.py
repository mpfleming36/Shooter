
from Entity import *
from Vector2 import *
from CollisionManager import *
from Enemy import *
import pygame

'''
Larger size and slower speed bullet
'''
class RocketBullet(Entity):

    def __init__(self, spawnX, spawnY, aimX, aimY, speed):
        self.speed = speed
        Entity.__init__(self, spawnX, spawnY, 20, 20, aimX*speed, aimY*speed)
        self.isAlive = True
        self.hitPoints = 1
        self.colBoxAnchorOffset = Vector2(0,0)
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                                self.position.y + self.colBoxAnchorOffset.y, 
                                                                self.dimensions.x, self.dimensions.y, self)
    
    def handleBoundHit(self, direction):
        #base functionality, if I go off the screen, I die
        if(direction[0] != 0 or direction[1] != 0):
            self.isAlive = False
            self.hitPoints = 0
            self.updateCollisionBox()
        
    def moveIt(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.updateCollisionBox()
    
    def drawIt(self,screen):
        pygame.draw.rect(screen, (255,255,0), self.toRect())
                    
    def update(self, screen, lowBound, upBound):
        self.moveIt()
        self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound))
        if(self.hitPoints == 0):
            self.isAlive = False
        if(self.isAlive==True):
            self.drawIt(screen)        