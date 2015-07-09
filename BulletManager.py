
from BaseBullet import *
from ShotBullet import *
from RocketBullet import *

'''
Bullet Manager for BaseBullets, ShotBullets, and RocketBullets
'''
class BulletManager():
    '''
    This is going to be a manager and factory class for bullets
    '''

    bulletList = []
    
    @staticmethod
    def buildBaseBullet(spawnX, spawnY, aimX, aimY, speed):
        #print "BulletManager.buildBaseBullet"
        temp = BaseBullet(spawnX, spawnY, aimX, aimY, speed)
        BulletManager.bulletList.append(temp)
        return temp
    
    @staticmethod
    def buildShotBullet(spawnX, spawnY, aimX, aimY, speed):
        temp = ShotBullet(spawnX, spawnY, aimX, aimY, speed)
        BulletManager.bulletList.append(temp)
        return temp
    @staticmethod
    def buildRocketBullet(spawnX, spawnY, aimX, aimY, speed):
        temp = RocketBullet(spawnX, spawnY, aimX, aimY, speed)
        BulletManager.bulletList.append(temp)
        return temp
    
    '''
    RemoveBullet from list function once dead, currently not using
    '''
    @staticmethod
    def removeBullet(self):
        print "removing"
        found = False
        i = 0
        while(found == False):
            if(BulletManager.bulletList[i].owner == self):
                del BulletManager.bulletList[i]
                found = True
            i += 1
    @staticmethod
    def update(screen, lowBound, upBound):
        for bullet in BulletManager.bulletList:
            if(bullet.isAlive == True):
                bullet.update(screen, lowBound, upBound)
                
    def __init__(self, params):
        '''
        Constructor
        '''
        