#FIXME: Monster is functional, but needs to be polymorphic. Add all the monsters into a group, and make all the function relating to them
#act on the group. there are pygame functions for this. 

#add references from th eoverhead file for: WINX, WINY, FRAMERATE, DISPLAYSURF
#This is the file for the main game loop, seperated from the class
#implementation for bip yum
import pygame, sys
from SlimesDelight import *
import SlimesDelight #Slimy Behavior
from GroundMaker import *
import GroundMaker # Draws the Background
from pygame.locals import *
from MonsterMash import *
import MonsterMash
import Armory
from Armory import *

import logging
logging.basicConfig(filename='MainLog.txt', level=logging.INFO, format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')

def Game(X,Y,DISPLAY, FrPrS):
	fpsClock = pygame.time.Clock()
	pygame.key.set_repeat(20)
	FPS =  FrPrS# frames per second setting, there is a copy in BIPYUM1 that should be the same
	# set up the window
	#Im gonna comment this out, but put it in the overhead file
	#                       DISPLAYSURF = pygame.display.set_mode((WINX, WINY), 0, 32)
	DISPLAYSURF = DISPLAY

	pygame.display.set_caption('Bip Yum')
	WHITE = (255, 255, 255)
	pygame.display.set_icon(slimeImg)w
	BackGround = BuildTheLand(WINX, WINY)
	slime = Slime()
	monster = Monster()
	monster.statBlock.setPos((100,100))
	#THis is a container to hold the weapons. It will hold a dirtySprite weapon, that way it can be made
	#to appear and disappear with each swing
	weapons = pygame.sprite.Group()
	sword = Weapon()
	weapons.add(sword)
	#This is where the little man is born, keep track of it

	#Trying to do the fight scenes in another program isnt working, so I need this main part to
	#Move to another part locally, otherwie it keeps executing the true loop, causing major bugs.

	#I've decided to do an action-RPG instead (A-la a Link to the Past.) Instead of having a battle scene, its
	#Gonna be a sword swing action, tied to the mouse click)
	logging.info("Game Initialized")
	while True: # the main game loop
		#Instead of filling with white, lets make a tiling of the background and blit it here
		BackGround.draw(DISPLAYSURF)
		slime.update()
		weapons.update(slime)
		#draw Slime to the screen, with any potential updates accounted for. 
		if(monster.statBlock.HEALTH > 0):
			monster.update(slime)
			DISPLAYSURF.blit(monster.image, (monster.position))
			DISPLAYSURF.blit(monster.statBlock.HealthBar.HPBAR_SURFACE, (monster.position))
		#this checks to see if slime is touched by an enemy.
			if(pygame.Rect.colliderect(slime.rect.inflate(-5,-5), monster.rect)):
				slime.takeDamage(monster)
		DISPLAYSURF.blit(slime.image, slime.position)
		if(sword.swing):
			weapons.draw(DISPLAYSURF)
			if(pygame.sprite.collide_rect(sword, monster) and monster.statBlock.HEALTH > 0):
				#logging.info("Enemy has been hit by sword")
				monster.takeDamage(slime)
		if(slime.statBlock.HEALTH <= 0):
			exit()

	   

	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()   
		pygame.display.update()
		fpsClock.tick(FPS)
