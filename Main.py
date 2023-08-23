import pygame, sys
import logging
import TitleScreen
pygame.init()
#this gets the current display surface and sets it to DISPLAYSURF. THis allows THe screen to be passed as a parameter
DISPLAYSURF = pygame.display.get_surface()
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(20)
FPS =  50# frames per second setting, there is a copy in BIPYUM1 that should be the same
#FIXME: WINDOW SIZES SHOULD BE READ IN FROM ADJACENT FILE
WINX = 600
WINY = 600

TitleScreen.Title(WINX, WINY, DISPLAYSURF, FPS)


#THe main game loop here is pretty complex. 
#first, start the game by loading it to the title screen.
#when the user makes certain selections from the title screen, it will return here. 
#start the game as an old or new file based on that selection.
#from there, send it to Game.py's main loop, which currently terminates when the player presses Q
#should the player ever quit, send them back to the title screen. 