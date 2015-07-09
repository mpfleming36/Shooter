
from Gun import *
from Vector2 import *
from BulletManager import *
import pygame

'''
Shoots one bullet at a time.
Slowest fire rate
Largest bullets
'''
class RocketGun(Gun):
    '''
    classdocs
    '''
    def __init__(self, mount, aimVector):
        Gun.__init__(self, mount, aimVector)
        self.delay = 750
        self.bulletSpeed = 5
        self.timer = pygame.time.get_ticks()
        self.isRapidFire = True
        
    def shoot(self):
        #print "machinegun.shoot", self.canShoot
        if self.canShoot:
            self.timer = pygame.time.get_ticks()
            self.generateBullets()
    
    def generateBullets(self):
        BulletManager.buildRocketBullet(self.origin.x, self.origin.y, 
                                      self.aimVector.x, self.aimVector.y, self.bulletSpeed)