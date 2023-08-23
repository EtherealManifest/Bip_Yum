import pygame, sys

buttonFont = pygame.font.Font("Planet Comic.otf", size = 12)
class Button(pygame.sprite.Sprite):
    xPos = 0
    yPos = 0
    text = ''
    xSize = 0
    ySize = 0
    backColor = (0,0,0)
    def __init__(self, pos, Text, Xsize, Ysize):
        pygame.sprite.Sprite.__init__(self)
        self.xPos = pos[0]
        self.yPos = pos[1]
        self.text = Text
        self.xSize = Xsize
        self.ySize = Ysize
        #set button rectangle position
        self.rect.x,self.rect.y = self.xPos, self.yPos
        #set botton rectangle size
        self.rect.width,self.rect.height = self.xSize, self.ySize
        #default to a white button
        self.backColor = (255,255,255)
        #this is the offical documentation for drawing a rectangle. if I return a surface, it will be blittable to another surface
            #rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, 
            #border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

        #set the surface color and border color. THe border will be the background, then a smaller shape will be layered on top.
        def mkButton(width, height, color, border_width):

            inner = pygame.Surface(width - border_width, height - border_width)
            outer = pygame.Surface(width, height)

            #format inner to the correct form, then blit it onto the outer and return the outer button. 
            pygame.rect.draw(inner, color, pygame.rect(width - border_width, height - border_width), radius = 5)

            #format outer to have the same curved edges that inner does
            pygame.rect.draw(outer, (0,0,0), pygame.rect(width, height), radius = 5)

            outer.blit(inner)

            return outer

        def addText(button, text, size):
            #create a new font Surface, whose height is slightly smaller than the button height
            buttonFont = pygame.font.Font("Planet Comic.otf", size = button.get_size[0] - 10)
            Texts = pygame.font.buttonFont.render(text)
            #blit the text to the button, then return it. make sure it is centered when it is blit
            button.blit(Texts, ((button.get_width - Texts.get_width)/2), ((button.get_height- Texts.get_height)/2))
