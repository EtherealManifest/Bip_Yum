import pygame
from pygame.locals import *
import random
import sys
import GroundMaker
import os
from pathlib import Path

# in meta, the size of the screen is recorded. Get it
META = (open('Meta.txt').read()).split(':')
WINX = int(META[0])
WINY = int(META[1])
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(20)
FPS = int(META[3]) - 30  # frames per second setting

#this is for the BIP YUM text, it will be 1/5 at high as the screen
font = pygame.font.SysFont("Times New Roman", int(WINY/5))
NameOfTheGame = font.render("Bip Yum", False, (255,225,255))
GameNamePOS = (((WINX / 2) - NameOfTheGame.get_width()/2), (WINY/2) - NameOfTheGame.get_height()/2)


openSky = pygame.Surface((WINX, WINY))
cloudArray = []
# Cloud list, which is used to put the actual clouds in the actual sky
cloudList = os.listdir('./CloudSprites/')

for panel in cloudList:
    temp = Path('./CloudSprites/' + panel)
    cloudArray.append(pygame.image.load(temp))

cloudGroup = pygame.sprite.Group()
cloudMoveSpeed = 1
#number of clouds to render
cloudNum = 6
# cloud move direction will be 1-8, and each will be a 45 degree clockwise angle from the last
# 1 = left
cloudMoveDirection = 1




# add a method that will paint the background blue and set some clouds to scroll
# across the screen. THis will be the background.
    # declared Variables

    # this class is the object for each cloud
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
        if (self.pos[0] < -self.rect.width):
            self.pos[0], self.pos[1] = (WINX, (random.randint(0, WINY)))
        #now update the blitting location
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

def setTheSkies():
    for i in range(0, cloudNum + 1):
        newCloud = Cloud()
        cloudGroup.add(newCloud)
def runTitle(DISPLAYSURF):
    #Program Start:
    openSky.fill((25, 186, 255))
    setTheSkies()
    #I want to be able to scale the clouds. in order to do that, they need to
    # be surfaces, not sprites. I'm gonna add an intermediary that converts them
    # to a surface, then blits the surfaces together.
    cloudGroup.draw(openSky)
    DISPLAYSURF.blit(openSky, (0,0))
    Grass = GroundMaker.PlantTheGrass(WINX, WINY)

    #buttons

    #title Text:

    while True:
        cloudGroup.update()
        #when the user makes a selection, return the selection to Game.py
        openSky.fill((25,186,255))
        cloudGroup.draw(openSky)
        Grass.draw(openSky)
        DISPLAYSURF.blit(openSky, (0,0))
        # blit the text onto the screen
        DISPLAYSURF.blit(NameOfTheGame, GameNamePOS)


        #poll for user input.
        #if they click the "Game" Button,
        #create a "Game" event and put it on the queue, then return to the
        #Game.py Loop.


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)


