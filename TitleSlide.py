import pygame
from pygame.locals import *
import random
import sys
import GroundMaker
import os
from pathlib import Path
import Button

# in meta, the size of the screen is recorded. Get it
META = (open('Meta.txt').read()).split(':')
WINX = int(META[0])
WINY = int(META[1])
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(20)
FPS = int(META[3])  # frames per second setting

#this is for the BIP YUM text, it will be 1/5 at high as the screen
font = pygame.font.SysFont("Planet Comic", int(WINY/5))
NameOfTheGame = font.render("Bip Yum", False, (0,0,0))
GameNamePOS = (((WINX / 2) - NameOfTheGame.get_width()/2), (WINY/2) - NameOfTheGame.get_height()/2)



cloudArray = []
# Cloud list, which is used to put the actual clouds in the actual sky
cloudList = os.listdir('./CloudSprites/')
for panel in cloudList:
    temp = Path('./CloudSprites/' + panel)
    cloudArray.append(pygame.image.load(temp))

cloudGroup = pygame.sprite.Group()
cloudMoveSpeed = .4
#number of clouds to render
cloudNum = 6
# cloud move direction will be 1-8, and each will be a 45 degree clockwise angle from the last
# 1 = left
cloudMoveDirection = 5



#This class declares coulds and gives them a position. It has methods for
#redrawing clouds on the other side of the screen
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # pick a random cloud sprite
        valid = False
        while not valid:
            self.image = random.choice(cloudArray)
            # define its bounding box
            self.rect = self.image.get_rect()
            valid = self.rect.width < WINX and self.rect.height < WINY
        # give it a position value that will always place it on the screen
        self.pos = [random.randrange(0, WINX - self.rect.width), random.randrange(0, WINY - self.rect.height)]
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

    def update(self):
        # updating the clouds bascially involves moving them.
        # if the cloud goes off screen, remove it from the group and
        # place it on the far edge of teh screen
        if cloudMoveDirection == 1:
            self.pos[0] -= cloudMoveSpeed
            self.pos[1] += 0
        elif cloudMoveDirection == 2:
            self.pos[0] -= cloudMoveSpeed
            self.pos[1] -= cloudMoveSpeed
        elif cloudMoveDirection == 3:
            self.pos[0] -= 0
            self.pos[1] -= cloudMoveSpeed
        elif cloudMoveDirection == 4:
            self.pos[0] += cloudMoveSpeed
            self.pos[1] -= cloudMoveSpeed
        elif cloudMoveDirection == 5:
            self.pos[0] += cloudMoveSpeed
            self.pos[1] += 0
        elif cloudMoveDirection == 6:
            self.pos[0] += cloudMoveSpeed
            self.pos[1] += cloudMoveSpeed
        elif cloudMoveDirection == 7:
            self.pos[0] -= 0
            self.pos[1] += cloudMoveSpeed
        elif cloudMoveDirection == 8:
            self.pos[0] -= cloudMoveSpeed
            self.pos[1] += cloudMoveSpeed
        # if the cloud is completely off screen, set it to a random height and
        # scroll it from the other side
        if (self.pos[0] < -self.rect.width - 60):
            self.pos[0], self.pos[1] = (WINX, (random.randint(0, WINY)))
        #now update the blitting location
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

def setTheSkies():
    for i in range(0, cloudNum + 1):
        newCloud = Cloud()
        cloudGroup.add(newCloud)

def changeTheSkies(currClouds):
    for cloud in currClouds:
        if cloud.pos[0] < -cloud.rect.width:
            cloud = Cloud()


#this is the loop that runs the title screen
def runTitle(DISPLAYSURF):
    #Program Start:
    openSky = pygame.Surface((WINX, WINY))
    openSky.fill((25, 186, 255))
    setTheSkies()
    #I want to be able to scale the clouds. in order to do that, they need to
    # be surfaces, not sprites. I'm gonna add an intermediary that converts them
    # to a surface, then blits the surfaces together.
    cloudGroup.draw(openSky)
    DISPLAYSURF.blit(openSky, (0,0))
    Grass = GroundMaker.PlantTheGrass(WINX, WINY)
    #buttons
    button_list = []
    start_button = Button.Button()
    quit_button = Button.Button()
    start_button.modify(_pos = (WINX/2 - start_button.get_rect().width/2, 2*WINY/3), _text = "START",
                        _label = "start-button")
    button_list.append(start_button)
    quit_button.modify(_pos = (start_button.pos[0],
                               start_button.pos[1] + 2 * start_button.height),
                       _text = "QUIT",
                       _label = 'quit-button')
    button_list.append(quit_button)


    #title Text
    while True:
        changeTheSkies(cloudGroup)
        cloudGroup.update()
        #when the user makes a selection, return the selection to Game.py
        openSky.fill((25,186,255))
        cloudGroup.draw(openSky)
        Grass.draw(openSky)
        DISPLAYSURF.blit(openSky, (0,0))
        # blit the text onto the screen
        DISPLAYSURF.blit(NameOfTheGame, GameNamePOS)
        #Load the button
        for button in button_list:
            DISPLAYSURF.blit(button, button.pos)
            button.is_hovered = False

        # check to see if the mouse is positioned over the start button
        for button in button_list:
            if(button.isHovered(pygame.mouse.get_pos())):
                #set the cursor to a focused cursor
                button.is_hovered = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                #if the left button is clicked
                if(pygame.mouse.get_pressed()[0]):
                    button.is_clicked = True
            status = button.update()
            if status != "":
                return status

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'Q'


        pygame.display.update()
        fpsClock.tick(FPS)