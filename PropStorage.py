#Define the setpieces to be used here
import SetPeice, os,pygame
from pathlib import Path


sceneShop = []
setPieceList = os.listdir('./setPiecePanels')



#get all the default sprites(only ones currently generated)
#for each sprite in the listed directory
#get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    sceneShop.append(pygame.image.load(temp))
class DefaultSetPiece(SetPeice.setPiece):
    def __init__(self):
        super().__init__()
        self.image = sceneShop[0]
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (99,123))
        self.isPassable = False

DEFAULTSETPIECE = DefaultSetPiece()


