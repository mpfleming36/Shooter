
from Gun import *
from Vector2 import *
from BulletManager import *
import pygame

'''
Shoots 3 bullets at once. Currently only at a lower and higher y, not angle based
Normal fire rate
Smallest bullets
'''
class ShotGun(Gun):
    '''
    classdocs
    '''
    def __init__(self, mount, aimVector):
        Gun.__init__(self, mount, aimVector)
        self.delay = 500
        self.bulletSpeed = 10
        self.timer = pygame.time.get_ticks()
        self.isRapidFire = True
        
    def shoot(self):
        #print "machinegun.shoot", self.canShoot
        if self.canShoot:
            self.timer = pygame.time.get_ticks()
            self.generateBullets()
    
    def generateBullets(self):
        BulletManager.buildShotBullet(self.origin.x, self.origin.y, 
                                      self.aimVector.x, self.aimVector.y, self.bulletSpeed)
        BulletManager.buildShotBullet(self.origin.x, self.origin.y+15, 
                                      self.aimVector.x, self.aimVector.y, self.bulletSpeed)
        BulletManager.buildShotBullet(self.origin.x, self.origin.y-15, 
                                      self.aimVector.x, self.aimVector.y, self.bulletSpeed)
        
'''
Currently not based off angles.
'''