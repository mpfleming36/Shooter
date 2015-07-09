
from Player import *

class PlayerInputController():
    '''
    This class is an inbetween for handling and calling input events in a player
    This class allows us to easily change key bindings
    '''

    #constructor sets up initial bindings for keys
    def __init__(self, up, down, left, right, act1, act2, key1, key2, key3, player):
        self.upKey = up
        self.downKey = down
        self.leftKey = left
        self.rightKey = right
        self.actionKey1 = act1
        self.actionKey2 = act2
        self.keyOne = key1
        self.keyTwo = key2
        self.keyThree = key3
        
        self.owningPlayer = player

    '''
    up
    down
    right
    left
    shoot
    change weapon
    weapon1
    weapon2
    weapon3
    '''
    def update(self, keyboard):
        if(keyboard[self.upKey] == True):
            self.owningPlayer.inputUpKeyAction()
        #else:
            #self.owningPlayer.inputUpKeyRelease()
        if(keyboard[self.downKey] == True):
            self.owningPlayer.inputDownKeyAction()
        
        if(keyboard[self.rightKey] == True):
            self.owningPlayer.inputRightKeyAction()
        
        if(keyboard[self.leftKey] == True):
            self.owningPlayer.inputLeftKeyAction()
        
        if(keyboard[self.actionKey1] == True):
            self.owningPlayer.inputAction1()
        #else:
            #self.owningPlayer.releaseAction1()
            
        if(keyboard[self.actionKey2] == True):
            self.owningPlayer.inputAction2()
            
        if(keyboard[self.keyOne] == True):
            self.owningPlayer.inputKey1()
        if(keyboard[self.keyTwo] == True):
            self.owningPlayer.inputKey2()
        if(keyboard[self.keyThree] == True):
            self.owningPlayer.inputKey3()
            
            
        