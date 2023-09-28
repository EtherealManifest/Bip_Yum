import pygame, sys, random, os
from pathlib import Path
from pygame.locals import *
pygame.init()


# this is the path to the panel folder, the loop below it loads all of them in to the
# grasspanels list, which is used to build the background
panelList = os.listdir('./GroundPanels/')

grassTiles = []
#These are grass tiles. they are all 100 px x 100 px
for panel in panelList:
    temp = Path('./GroundPanels/' + panel)
    grassTiles.append(pygame.image.load(temp))


# loads the plant panels in, just like the grass panels
plantTiles = []
panelList = os.listdir('./PlantPanels/')
for panel in panelList:
    temp = Path('./PlantPanels/' + panel)
    plantTiles.append(pygame.image.load(temp))

ThePlants = pygame.sprite.Group()

class Grass(pygame.sprite.Sprite):
    position = (0,0)
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.position = (0,0)

class Plant(pygame.sprite.Sprite):
    position = (0,0)
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.position = (0,0)
    def update(DispSurf, self):
        ThePlants.draw(DispSurf)







TheLand = pygame.sprite.Group()



def BuildTheLand(width, height):
#this loop adds random tiles to the
    for i in range(0, width + 1, 100):
        for j in range(0, height + 1, 100):
            selec = random.choice(grassTiles)
            selec = Grass(selec)
            selec.rect.x = j
            selec.rect.y = i
            TheLand.add(selec)
    return TheLand

#this method is used by TitleScreen to create the grass that makes up the bottom of the screen
#It also stoes three frames of animation for them. 

def PlantTheGrass(width, height):
    for i in range(0, width + 1, 64):
        selec = random.choice(plantTiles)
        selec = Plant(selec)
        selec.rect.x = i
        selec.rect.y = height - 64
        ThePlants.add(selec)
    return ThePlants
            

        

