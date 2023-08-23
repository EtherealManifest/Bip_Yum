import pygame, sys
from pygame.locals import *
import GroundMaker


def Title(X,Y,DISPLAY,FPS):
    fpsClock = pygame.time.Clock()
    pygame.key.set_repeat(20)

    
    WINX = X       #THese are defaults, I want to add a fullscreen option that will import the systems default fullscreen size. 
    WINY = Y

    DISPLAYSURF = DISPLAY
    WHITE = (255, 255, 255)
    SKY_BLUE = (96, 205, 247)
    
    #main loop
    while(True):
        #set the background to Blue
        DISPLAYSURF.fill((SKY_BLUE))
        #set the clouds to be randomly generated and move from left to right at varying speeds

        #set the grass to take up the entire bottom of the screen
        lowerGrass = GroundMaker.PlantTheGrass(WINX, WINY)
        lowerGrass.draw(DISPLAYSURF)

        #add buttons for play, new game, options, and quit.
        #create a button object and then customize it
        #Poll for input. If a player clicks on any of the buttons, then respond accordingly. 


        #OPTIONS SUBMENU
        #NEW GAME CONFIRM
        #QUIT CONFIRM


