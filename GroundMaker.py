import pygame, sys, random, os
from pathlib import Path
from pygame.locals import *

pygame.init()

# this is the path to the panel folder, the loop below it loads all of them in to the
# grasspanels list, which is used to build the background

landTiles = []
TheLand = pygame.sprite.Group()
plantTiles = []
ThePlants = pygame.sprite.Group()
# These are grass tiles. they are all 100 px x 100 px

# loads the plant panels in, just like the grass panels
# FOR THE SCENARIO UPDATE::
# READ IN FROM THE SCENARIO WHICH DIRECTORY TO PULL FROM
panelList = os.listdir('./PlantPanels/')
for panel in panelList:
    temp = Path('./PlantPanels/' + panel)
    plantTiles.append(pygame.image.load(temp))


# FOR THE SCENARIO UPDATE:
# READ IN THE LIST OF CREATED SET PIECES AND ADD THEM TO
# ANOTHER GROUP. THIS GROUP WILL BE RETURNED TO THE MAIN GAME LOOP
# THE REASON FOR THIS IS THAT THE MAIN GAME LOOP NEEDS TO BE ABLE
# TO SEE THE PROPERTIES OF EVERY SETPIECE.
# THE SETPEICES WILL BE BLIT ONTO THE MAP NORMALLY

class Land(pygame.sprite.Sprite):
    position = (0, 0)

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.position = (0, 0)


class Plant(pygame.sprite.Sprite):
    position = (0, 0)

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.position = (0, 0)

    def update(DispSurf, self):
        ThePlants.draw(DispSurf)


def BuildTheLand(width, height, locale=Path('./GroundPanels/Grass')):
    # this loop adds random tiles to the land group. it then "stitches" them all together
    # And returns them as a group.
    # search the given folder, and get the list of land tiles
    # search the given folder, and get the list of land tiles
    panelList = os.listdir(locale)
    for panel in panelList:
        temp = Path(str(locale) + '\\' + panel)
        landTiles.append(pygame.image.load(temp))

    for i in range(0, width + 1, 100):
        for j in range(0, height + 1, 100):
            selec = random.choice(landTiles)
            selec = Land(selec)
            selec.rect.x = j
            selec.rect.y = i
            TheLand.add(selec)
    return TheLand


# this method is used by TitleScreen to create the grass that makes up the bottom of the screen
# It also stoes three frames of animation for them.
def PlantTheGrass(width, height):
    for i in range(0, width + 1, 64):
        selec = random.choice(plantTiles)
        selec = Plant(selec)
        selec.rect.x = i
        selec.rect.y = height - 64
        ThePlants.add(selec)
    return ThePlants
