
from Entity import *

'''
Enemy base class
'''
class Enemy(Entity):
    
    def __init__(self, x,y,width,height,vx,vy):
        '''
        Constructor
        '''
        Entity.__init__(self, x, y, width, height, vx, vy)

    def handleBoundHit(self, direction):
        pass
    def aiPath(self, player):
        pass
    def update(self, drawTarget, lowBound, upBound,other):
        pass