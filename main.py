

import sys
import pygame
import random
from CollisionManager import *
from PlayerInputManager import *
from ActionPlayer import *
from Colors import *
from Entity import *
from BaseBullet import *
from BulletManager import *
from Enemy import *
from DumbEnemy import *
from SmartEnemy import *
from pygame.time import delay

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
UIBoard = pygame.font.SysFont("monospace", 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

'''
Main game function, creates Player and Enemies
Sets gameState, difficulty, and score.
''' 
def main():
    gameState = 0
    difficulty = 1
    score = 0
    del BulletManager.bulletList[:]
    del CollisionManager.collisionList[:]
    myPlayer = None
    myPlayer = PlayerInputManager.buildActionPlayer(pygame.K_w, 
                                                    pygame.K_s, 
                                                    pygame.K_a, 
                                                    pygame.K_d, 
                                                    pygame.K_SPACE,
                                                    pygame.K_e,
                                                    pygame.K_1,
                                                    pygame.K_2,
                                                    pygame.K_3, 
                                                    SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 
                                                    100, 100, 
                                                    5, 5)
    theEnemy = []
    theEnemy.append(DumbEnemy(50,150,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(50,250,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(50,350,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(50,450,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(50,550,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(50,650,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(150,50,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(250,50,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(350,50,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(450,50,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(550,50,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(650,50,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(750,150,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(750,250,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(750,350,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(750,450,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(750,550,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(750,650,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(650,750,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(550,750,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(450,750,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(350,750,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(250,750,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(DumbEnemy(150,750,25,25,random.randint(0,2),random.randint(0,2)))
    theEnemy.append(SmartEnemy(750,50,50,50,3,3))
    theEnemy.append(SmartEnemy(50,50,50,50,3,3))
    theEnemy.append(SmartEnemy(750,750,50,50,3,3))
    theEnemy.append(SmartEnemy(50,750,50,50,3,3))
    
    
        
    while(True):
        screen.fill(Color.black)
        
        
        '''
        States how to start the game and to change the difficulty.
        Also tells the user the controls.
        '''
        if (gameState == 0):
            welcomeLabel = UIBoard.render(str("Welcome to Shooter Game"), 1, Color.white)
            screen.blit(welcomeLabel, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2-300))
            welcomeLabel = UIBoard.render(str("Difficulty: ")+str(difficulty), 1, Color.white)
            screen.blit(welcomeLabel, (SCREEN_WIDTH/2-125, SCREEN_HEIGHT/2-250))
            difficultyLabel = UIBoard.render(str("Press 1 2 3 for Difficulty"), 1, Color.white)
            screen.blit(difficultyLabel, (SCREEN_WIDTH/2-225, SCREEN_HEIGHT/2-150))
            startLabel = UIBoard.render(str("Press Space to Play"), 1, Color.white)
            screen.blit(startLabel, (SCREEN_WIDTH/2-175, SCREEN_HEIGHT/2-100))
            wepLabel = UIBoard.render(str("In Game Press 1 2 3 to Switch Guns"), 1, Color.white)
            screen.blit(wepLabel, (SCREEN_WIDTH/2-275, SCREEN_HEIGHT/2+150))
            shootLabel = UIBoard.render(str("In Game Space to Shoot"), 1, Color.white)
            screen.blit(shootLabel, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2+200))
            keyboard = pygame.key.get_pressed()
            if(keyboard[pygame.K_SPACE]):
                gameState = 1
            if(keyboard[pygame.K_1]):
                difficulty = 1
                for i in range(0, len(theEnemy)):
                    if(isinstance(theEnemy[i], DumbEnemy)):
                        theEnemy[i].hitPoints = 1
                    elif(isinstance(theEnemy[i], SmartEnemy)):
                        theEnemy[i].hitPoints = 10
            if(keyboard[pygame.K_2]):
                difficulty = 2
                for i in range(0, len(theEnemy)):
                    if(isinstance(theEnemy[i], DumbEnemy)):
                        theEnemy[i].hitPoints = 2
                    elif(isinstance(theEnemy[i], SmartEnemy)):
                        theEnemy[i].hitPoints = 20
            if(keyboard[pygame.K_3]):
                difficulty = 3
                for i in range(0, len(theEnemy)):
                    if(isinstance(theEnemy[i], DumbEnemy)):
                        theEnemy[i].hitPoints = 3
                    elif(isinstance(theEnemy[i], SmartEnemy)):
                        theEnemy[i].hitPoints = 30
            
        '''
        Gamestate that is the actual game, updates enitities, shows health and score.
        '''
        if (gameState == 1):
            healthLabel = UIBoard.render("HEALTH: " + str(myPlayer.hitPoints), 1, Color.white)
            screen.blit(healthLabel, (SCREEN_WIDTH-250, SCREEN_HEIGHT-25))
            scoreLabel = UIBoard.render("KILLS: " + str(score), 1, Color.white)
            screen.blit(scoreLabel, (50, SCREEN_HEIGHT-25))
            count = 0
        #eventually we'll need the collision manager update here as well
            if(myPlayer.collisionBox.isAlive == True):
                PlayerInputManager.update(pygame.key.get_pressed())
                myPlayer.update(screen, [10,10], [SCREEN_WIDTH-10, SCREEN_HEIGHT-10])
            else:
                gameState = 2
            for i in range(0, len(theEnemy)):
                if(theEnemy[i].isAlive == True):
                    theEnemy[i].update(screen, [0,0], [SCREEN_WIDTH, SCREEN_HEIGHT], myPlayer)
                    for j in range(0, len(BulletManager.bulletList)):
                        theEnemy[i].update(screen, [0,0], [SCREEN_WIDTH, SCREEN_HEIGHT], BulletManager.bulletList[j])
                else:
                    count+=1
                theEnemy[i].aiPath(myPlayer)
            BulletManager.update(screen, [0,0], [SCREEN_WIDTH, SCREEN_HEIGHT])
            score = count
            if(score == 28):
                gameState = 3
            
        '''
        Lets user know they lost, gives option to start again
        resets main
        '''    
        if (gameState == 2):
            lostLabel = UIBoard.render(str("You Lose"), 1, Color.white)
            screen.blit(lostLabel, (SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2))
            restartLabel = UIBoard.render(str("Press 'R' to Play Again"), 1, Color.white)
            screen.blit(restartLabel, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2+50))
            keyboard = pygame.key.get_pressed()
            if(keyboard[pygame.K_r]):
                main()
                gameState = 0
        
        ''' 
        Lets user know they won, gives option to start again
        resets main
        '''         
        if (gameState ==3):
            wonLabel = UIBoard.render(str("You Won"), 1, Color.white)
            screen.blit(wonLabel, (SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2))
            restartLabel = UIBoard.render(str("Press 'R' to Play Again"), 1, Color.white)
            screen.blit(restartLabel, (SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2+50))
            keyboard = pygame.key.get_pressed()
            if(keyboard[pygame.K_r]):
                main() 
                gameState = 0
            
                
        msElapsed = clock.tick(30) #SYNC RATE 30 FPS
        pygame.display.update() #SYNC 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();


if __name__ == '__main__':
    main()