import pygame, sys, random
from pygame.locals import *
pygame.init()

#These are grass tiles. they are all 100 px x 100 px
Grass0 = pygame.image.load('Grass_0.png')
Grass1 = pygame.image.load('Grass_1.png')
Grass2 = pygame.image.load('Grass_2.png')
Grass3 = pygame.image.load('Grass_3.png')
Grass4 = pygame.image.load('Grass_4.png')
Grass5 = pygame.image.load('Grass_5.png')
Grass6 = pygame.image.load('Grass_6.png')
Grass7 = pygame.image.load('Grass_7.png')

#these are plant tiles for the Title screen. They are sorted into groupd of three, each
#corresponding to a full animation cycle for one image. 
Plant0 = pygame.image.load('plant_sprite_0.png')
Plant1 = pygame.image.load('plant_sprite_1.png')

plantTiles = [Plant0,Plant1]
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





grassTiles = [Grass0, Grass1, Grass2, Grass3, Grass4, Grass5, Grass6, Grass7]

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
            

        

