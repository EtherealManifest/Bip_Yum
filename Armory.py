import pygame, sys
from pygame.locals import *
import SlimesDelight
from SlimesDelight import *
import logging
logging.basicConfig(filename='MainLog.txt', level=logging.INFO, format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')





weaponDefaultImg = pygame.image.load('sword_sprite_0.png')
#sets how long the sword swing lasts
SWINGTIME = 10
#These are placeholder animations
swordSwing1= pygame.image.load('sword_sprite_1.png')
swordSwing2= pygame.image.load('sword_sprite_2.png')
swordSwing3= pygame.image.load('sword_sprite_3.png')
swordSwing4= pygame.image.load('sword_sprite_4.png')

class Weapon(pygame.sprite.Sprite):
    
    #this is the position of the BOTTOM-CENTER of the weapon
    pos = (0,0)
    #The maximum reach, for determining the hitbox
    size = 0
    #This is for determining which way the weapon swings
    direction = ''
    facingRight = False
    #used to tell whether the sword is being swung
    swing = False
    #this determines the frame for the sword swing
    swingTick = 0

    def position(self, player):
        if(player.direction == 'up'):
            self.pos = (player.slimex + 32, player.slimey)
            self.facingRight = False
        elif(player.direction == 'down'):
            self.pos = (player.slimex + 32, player.slimey)
            self.facingRight = False 
        if (player.direction == 'down-left'
            or player.direction == 'left'
            or player.direction == 'up-left'):
            self.pos = (player.slimex - 8 , player.slimey - 16)
            self.facingRight = False
        elif(player.direction == 'down-right'
            or player.direction == 'right'
            or player.direction == 'up-right'):
            self.pos = (player.slimex + 32, player.slimey - 16)
            self.facingRight = True
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.direction = player.direction
        

    def __init__(self):
        #this initializes it as a Sprite
        pygame.sprite.Sprite.__init__(self)
        #these are Sprite Attributes
        self.pos = (0,0)
        self.image = weaponDefaultImg
        #effectively, the Hitbox
        self.rect = self.image.get_rect()
        self.direction = ''
        swing = False
        swingTick = 0
        facingRight = False
        

    def update(self, player):
        #it is positioned at the top of the slime, then moved back to
        #center the blade.
        #MAY NEED TUNING
        #this will all be implemented in position()
        self.position(player)
        self.image = weaponDefaultImg
        #the documentsataion said to call get() before get_pressed()
        pygame.event.get()
        #if the mouse is clicked, swing the sword
        #I'm gonna coordinae this as if he is facing left always.
        #if he faces right, Im going to just flip everything and move it
        if not self.swing:
            if pygame.mouse.get_pressed()[0]:
                self.swing = True
                self.swingTick = SWINGTIME
        
        if self.swing == True:
            if self.direction == 'up':
                if self.swingTick > SWINGTIME * .8:
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.pos = (self.rect.x, self.rect.y)
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .8) and self.swingTick >= int(SWINGTIME * .7):
                    #rotate the image 45 degrees and adjust the position
                    #move it a quarter of the body back and down
                    self.image = pygame.transform.rotate(self.image, -45)
                    self.pos = ((self.rect.x - int(player.rect.width * .6)), (self.rect.y - int(player.rect.height * 3/4)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .6) and self.swingTick >= int(SWINGTIME * .5):
                    #this part is straight up and down, no rotation necessary
                    self.image = weaponDefaultImg
                    self.pos = ((self.rect.x - player.rect.width * .9), (self.rect.y - player.rect.height))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .4) and self.swingTick >= int(SWINGTIME * .3):
                    self.image = pygame.transform.rotate(self.image, 45)
                    self.pos = ((self.rect.x - int(player.rect.width * 1.75)), (self.rect.y - int(player.rect.height * 3/4)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .2) and self.swingTick >= int(SWINGTIME * .1):
                    self.image = pygame.transform.rotate(self.image, 90)
                    self.pos = ((self.rect.x - int(player.rect.width * 2)), (self.rect.y - player.rect.y * 2))
                    self.rect.x = self.pos[0] 
                    self.rect.y = self.pos[1] 
                else:
                    self.swing = False

                    
            elif self.direction == 'down':
                if self.swingTick > SWINGTIME * .8:
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.pos = (self.rect.x, int(self.rect.y + player.rect.height * 3/4))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                    
                elif self.swingTick <= int(SWINGTIME * .8) and self.swingTick >= int(SWINGTIME * .7):
                    #rotate the image 45 degrees and adjust the position
                    #move it a quarter of the body back and down
                    self.image = pygame.transform.rotate(self.image, -135)
                    self.pos = ((self.rect.x - int(player.rect.width * .5)), (self.rect.y + int(player.rect.height * 7/8)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                    
                elif self.swingTick <= int(SWINGTIME * .6) and self.swingTick >= int(SWINGTIME * .5):
                    #this part is straight up and down, no rotation necessary
                    self.image = pygame.transform.rotate(self.image, -180)
                    self.pos = ((self.rect.x - player.rect.width * .9), (self.rect.y + player.rect.height * 1.25))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                    
                elif self.swingTick <= int(SWINGTIME * .4) and self.swingTick >= int(SWINGTIME * .3):
                    self.image = pygame.transform.rotate(self.image, 135)
                    self.pos = ((self.rect.x - int(player.rect.width * 1.8)), (self.rect.y + int(player.rect.height * 7/8)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                    
                elif self.swingTick <= int(SWINGTIME * .2) and self.swingTick >= int(SWINGTIME * .1):
                    self.image = pygame.transform.rotate(self.image, 90)
                    self.pos = ((self.rect.x - int(player.rect.width * 2.25)), int(self.rect.y + player.rect.height))
                    self.rect.x = self.pos[0] 
                    self.rect.y = self.pos[1]
                    
                else:
                    self.swing = False
                 
            elif (self.direction == 'left' or self.direction == 'down-left'
                or self.direction == 'up-left'):
                if self.swingTick > SWINGTIME * .8:
                    self.image = weaponDefaultImg
                    self.pos = ((self.rect.x + player.rect.width / 2), (self.rect.y))
                elif self.swingTick <= int(SWINGTIME * .8) and self.swingTick >= int(SWINGTIME * .7):
                    #rotate the image 45 degrees and adjust the position
                    #move it a quarter of the body back and down
                    self.image = pygame.transform.rotate(self.image, 45)
                    self.pos = ((self.rect.x - int(player.rect.width * 3/4)), (self.rect.y + int(player.rect.height/4)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .6) and self.swingTick >= int(SWINGTIME * .5):
                    self.image = pygame.transform.rotate(self.image, 90)
                    self.pos = ((self.rect.x - int(player.rect.width * .9)), (self.rect.y + int(player.rect.height)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .4) and self.swingTick >= int(SWINGTIME * .3):
                    self.image = pygame.transform.rotate(self.image, 135)
                    self.pos = ((self.rect.x - int(player.rect.width * 3/4)), (self.rect.y + int(player.rect.height * 6/5)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .2) and self.swingTick >= int(SWINGTIME * .1):
                    self.image = pygame.transform.rotate(self.image, 180)
                    self.pos = ((self.rect.x + player.rect.width / 4), (self.rect.y + player.rect.height * 9/7))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1] 
                else:
                    self.swing = False
            #if the player is facing right, then Acoomodate and adjust accordingly
            else:
                if self.swingTick > SWINGTIME * .8:
                    self.image = weaponDefaultImg
                    self.pos = ((self.rect.x - player.rect.width * 3/4), (self.rect.y))
                elif self.swingTick <= int(SWINGTIME * .8) and self.swingTick >= int(SWINGTIME * .7):
                    #rotate the image 45 degrees and adjust the position
                    #move it a quarter of the body back and down
                    self.image = pygame.transform.rotate(self.image, -45)
                    self.pos = ((self.rect.x + int(player.rect.width * .1)), (self.rect.y + int(player.rect.height/4)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .6) and self.swingTick >= int(SWINGTIME * .5):
                    self.image = pygame.transform.rotate(self.image, -90)
                    self.pos = ((self.rect.x + int(player.rect.width * .2)), (self.rect.y + int(player.rect.height)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .4) and self.swingTick >= int(SWINGTIME * .3):
                    self.image = pygame.transform.rotate(self.image, -135)
                    self.pos = ((self.rect.x + int(player.rect.width * .1)), (self.rect.y + int(player.rect.height * 6/5)))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1]
                elif self.swingTick <= int(SWINGTIME * .2) and self.swingTick >= int(SWINGTIME * .1):
                    self.image = pygame.transform.rotate(self.image, 180)
                    self.pos = ((self.rect.x - player.rect.width / 4), (self.rect.y + player.rect.height * 9/7))
                    self.rect.x = self.pos[0]
                    self.rect.y = self.pos[1] 
                else:
                    self.swing = False
                
            
                
                    
            #decrement the swing counter
            self.swingTick = self.swingTick - 1
            #logging.info("Weapon rect Coordinates (" + str(self.rect.x) + ", " + str(self.rect.y) + ")")
        

            
                
            
            

        
