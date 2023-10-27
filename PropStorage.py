#Define the setpieces to be used here
import SetPeice, os
from pathlib import Path
from pygame import image


sceneShop = []
setPieceList = os.listdir('./setPiecePanels')



#get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    sceneShop.append((image.load(temp), sprite))

DefaultSetPiece = SetPeice.setPiece()
DefaultSetPieceImg = sceneShop[1][0]
DefaultSetPieceRect = DefaultSetPieceImg.get_rect()

DefaultSetPiece.buildSetPiece(DefaultSetPieceImg, DefaultSetPieceRect, (99,123))

DEFAULTSETPIECE = DefaultSetPiece


