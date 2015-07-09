

from Enemy import *
from Vector2 import *
from CollisionManager import *
from Colors import *
from Player import *
from BaseBullet import *
from ShotBullet import *
from RocketBullet import *
import pygame
import math


'''
AI that just moves in the path given.
'''
class DumbEnemy(Enemy):
    
    def __init__(self, x,y,width,height,vx,vy):
        Enemy.__init__(self,x,y,width,height,vx,vy)
        self.colBoxAnchorOffset = Vector2(0,0) #since we have no art, this can be 0,0
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                              self.position.y + self.colBoxAnchorOffset.y,
                                                              width,height,
                                                              self)
        self.color = Color.green
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.hitPoints = 1

    
    def handleBoundHit(self, direction):
        #options:
        # - set up a flag preventing movement - basically turning off velocity in a direction
        # - set up a velocity backup variable and set velocity to 0?
        # - back the player up one velocity step
        if(direction[0] == -1):
            self.velocity.x = self.vx
        elif(direction[0] == 1):
            self.velocity.x = -self.vx
            
        if(direction[1] == -1):
            self.velocity.y = self.vy
        elif(direction[1] == 1):
            self.velocity.y = -self.vy
            
        self.updateCollisionBox()
    
    '''
    Draws the AI based off health
    '''  
    def drawIt(self,drawTarget):
        #using primitives for now ... sprites later
        if(self.hitPoints == 3):
            self.color = Color.green
        elif(self.hitPoints == 2):
            self.color = Color.yellow
        elif(self.hitPoints == 1):
            self.color = Color.red
        pygame.draw.rect(drawTarget,self.color,self.toRect())
        self.collisionBox.debugDraw(drawTarget)
    
    '''
    Controls how the AI moves
    '''      
    def aiPath(self,player):
        if(player.isAlive == True):
            self.position.x += self.velocity.x
            self.position.y += self.velocity.y
            #self.updateCollisionBox()
            
    '''
    How the AI deals with getting hit
    '''  
    def handleBoxHit(self, boxHit, other):
        if(boxHit):
            self.hitPoints -= 1
            if(self.hitPoints == 0):
                self.isAlive = False
            if(isinstance(other, Player)):
                other.hitPoints -= 1
            if(isinstance(other, BaseBullet)):
                other.hitPoints -= 1
                other.updateCollisionBox()
            if(isinstance(other, ShotBullet)):
                other.hitPoints -= 1
                other.updateCollisionBox()
            if(isinstance(other, RocketBullet)):
                other.hitPoints -= 1
                other.updateCollisionBox()
    
    '''
    Update AI
    '''  
    def update(self, drawTarget, lowBound, upBound, other):
        self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound))
        if (self.collisionBox.isAlive== True):
            self.handleBoxHit(self.collisionBox.checkBoxHit(other.collisionBox), other)
            self.drawIt(drawTarget)        
    