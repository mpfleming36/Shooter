
from Player import *
from Vector2 import *
from CollisionManager import *
from Colors import *
from MachineGun import *
from ShotGun import *
from RocketGun import *
import pygame
import math

class ActionPlayer(Player):
    '''
    ActionPlayer is a top-down arena shooter player character
    It will move in simple up/down/left/right & diagonal patterns
    It will eventually shoot through vectors at the mouse 
    Creates 3 weapons
    '''
    def __init__(self, x,y,width,height,vx,vy):
        Player.__init__(self,x,y,width,height,vx,vy)
        self.colBoxAnchorOffset = Vector2(0,0) #since we have no art, this can be 0,0
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                              self.position.y + self.colBoxAnchorOffset.y,
                                                              width,height,
                                                              self)
        self.shotty= ShotGun(Vector2(self.position.x + self.dimensions.x/2,
                                             self.position.y + self.dimensions.y/2),
                                     Vector2(1,1))
        self.smg = MachineGun(Vector2(self.position.x + self.dimensions.x/2,
                                             self.position.y + self.dimensions.y/2),
                                     Vector2(1,1))
        self.rockets = RocketGun(Vector2(self.position.x + self.dimensions.x/2,
                                             self.position.y + self.dimensions.y/2),
                                     Vector2(1,1))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.equipedGun = self.shotty
        self.gunColor = Color.ForestGreen
        self.gunSize = 5
        self.facing = Vector2(0,0)
        self.gunOrigin = Vector2(0,0)
        self.color = Color.purple3
        self.hitPoints = 20
        self.jumping = False
        self.gravity = 3
        
    '''
    inputs and what they do:
    up, down, right, left - all change position and constant velocity
    input1 tells where to shoot and when
    input2 changes the equipped weapon (currently buggy)
    1,2,3 - allows user to change to specific weapon
    '''
    #input hooks
    def inputUpKeyAction(self):
        self.position.y -= self.velocity.y
        self.updateCollisionBox()
        
    def inputDownKeyAction(self):
        self.position.y += self.velocity.y
        self.updateCollisionBox()
        

    def inputRightKeyAction(self):
        self.position.x += self.velocity.x
        self.updateCollisionBox()
        
    def inputLeftKeyAction(self):
        self.position.x -= self.velocity.x
        self.updateCollisionBox()
    
    def inputAction1(self):
        if(self.isAlive == True):
            self.equipedGun.update(self.gunOrigin,self.facing, True)
            self.equipedGun.shoot()
     
    def inputAction2(self):
        if (self.equipedGun == self.shotty):
            self.equipedGun = self.smg
            self.gunColor = Color.magenta
            self.gunSize = 7
            self.equipedGun.update(self.gunOrigin,self.facing, True)
        elif(self.equipedGun == self.smg):
            self.equipedGun = self.rockets
            self.gunColor = Color.gray
            self.gunSize = 10
            self.equipedGun.update(self.gunOrigin,self.facing, True)
        elif(self.equipedGun == self.rockets):
            self.equipedGun = self.shotty
            self.gunColor = Color.ForestGreen
            self.gunSize = 5
            self.equipedGun.update(self.gunOrigin,self.facing, True)
    
    def inputKey1(self):
        self.equipedGun = self.shotty
        self.gunColor = Color.ForestGreen
        self.gunSize = 5
    def inputKey2(self): 
        self.equipedGun = self.smg
        self.gunColor = Color.magenta
        self.gunSize = 7
    def inputKey3(self):
        self.equipedGun = self.rockets
        self.gunColor = Color.gray
        self.gunSize = 10
    
    #in our action game, we want to aim at the mouse
    #so we need the mouse location
    def calculateAimingVector(self):
        mousePos = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        midPoint = Vector2(self.position.x + self.dimensions.x/2, 
                           self.position.y + self.dimensions.y/2)
        
        vector = Vector2(mousePos.x - midPoint.x, mousePos.y - midPoint.y)
        if(vector.x != 0 or vector.y != 0):
            size = math.sqrt(vector.x**2 + vector.y**2)
            self.facing.x = vector.x/size
            self.facing.y = vector.y/size
    
    #calculates where the gun is based off mouse
    def calculateGunOrigin(self):
        self.calculateAimingVector() #update aiming vector
        midPoint = Vector2(self.position.x + self.dimensions.x/2, 
                           self.position.y + self.dimensions.y/2)
        self.gunOrigin.x = midPoint.x + (self.facing.x * 75)
        self.gunOrigin.y = midPoint.y + (self.facing.y * 75)
    
    def handleBoundHit(self, direction):
        #options:
        # - set up a flag preventing movement - basically turning off velocity in a direction
        # - set up a velocity backup variable and set velocity to 0?
        # - back the player up one velocity step
        if(direction[0] == -1):
            self.position.x += self.velocity.x
        elif(direction[0] == 1):
            self.position.x -= self.velocity.x
            
        if(direction[1] == -1):
            self.position.y += self.velocity.y
        elif(direction[1] == 1):
            self.position.y -= self.velocity.y
            
        self.updateCollisionBox()
    
    '''
    draws player, gun, and collision box
    '''
    def drawIt(self,drawTarget):
        pygame.draw.rect(drawTarget,self.color,self.toRect())
        pygame.draw.circle(drawTarget, self.gunColor, 
                            (int(self.gunOrigin.x), int(self.gunOrigin.y)),
                            self.gunSize)

        self.collisionBox.debugDraw(drawTarget)
    
    '''
    Update Player
    ''' 
    def update(self, drawTarget, lowBound, upBound):

        if(self.hitPoints <=0):
            self.collisionBox.isAlive = False
        if(self.collisionBox.isAlive == True):
            self.drawIt(drawTarget)
            self.calculateGunOrigin()  
            self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound))
        
    