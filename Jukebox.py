'''this module is designed to hold all the information
regarding the background music. Other python files
will call this with a keyword to have this
module play the background music'''
import pygame
from pathlib import Path



BattleMusicPath = Path('./Music(not Owned)/Meta Knight s Revenge.mp3')
BattleMusic = pygame.mixer.Sound(BattleMusicPath)