
from Entity import *

'''
Base Player Class
'''
class Player(Entity):
    
    def __init__(self, x,y,width,height,vx,vy):
        '''
        Constructor
        '''
        Entity.__init__(self, x, y, width, height, vx, vy)
        #I am an entity, so I have things like a collision box and offset, etc
        #however, I'm still an abstract so, I don't set those things yet
        
    #input hooks
    def inputUpKeyAction(self):
        pass
    def inputDownKeyAction(self):
        pass
    def inputRightKeyAction(self):
        pass
    def inputLeftKeyAction(self):
        pass
    
    def inputAction1(self):
        pass
    def inputAction2(self):
        pass
    
    def inputKey1(self):
        pass
    def inputKey2(self):
        pass
    def inputKey3(self):
        pass
        
    #more to come
    
    def handleBoundHit(self, direction):
        pass
    
    def update(self, drawTarget, lowBound, upBound):
        pass
    