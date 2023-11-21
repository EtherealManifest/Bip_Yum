import pygame

font = pygame.font.SysFont("System", 15)


class Button(pygame.surface.Surface):
    text = ""
    width = 0
    height = 0
    pos = (0, 0)
    background_color = (255, 255, 255, 255)
    label = ""

    def __init__(self):
        pygame.surface.Surface.__init__(self, (100, 20))
        self.text = "Click Me!"
        # blit this to the surface later
        self.width = 100
        self.height = 20
        self.pos = (0, 0)
        self.background_color = (255, 255, 255, 255)
        self.label = ""
        self.fill(self.background_color)
        buttonText = font.render(self.text, False, (0, 0, 0))
        self.blit(buttonText, (0, 0))
        self.is_clicked = False
        self.is_hovered = False
        self.textx = 0
        self.texty = 0

    def modify(self, _text="Click Me", _height=20, _width=100, _pos=(0, 0),
               _background_color=(255, 255, 255, 255), _label=""):
        self.text = _text
        # blit this to the surface later
        self.width = _width
        self.height = _height
        pygame.surface.Surface.__init__(self, (self.width, self.height))
        self.rect = self.get_rect()
        self.pos = _pos
        self.background_color = _background_color
        self.fill(self.background_color)
        self.label = _label
        global font
        font = pygame.font.SysFont("System", self.height)
        buttonText = font.render(self.text, False, (0, 0, 0))
        self.textx = (self.width / 2 - buttonText.get_width()/2)
        self.texty = (self.height / 2 - buttonText.get_height()/2)
        self.blit(buttonText, (self.textx, self.texty))
        self.is_clicked = False
        self.is_hovered = False

    #sets the background color to slightly less (mathematically) than the current background color.
    def hovered(self):
        temp_color =(
            self.background_color[0] - 50,
            self.background_color[1] - 50,
            self.background_color[2] - 10
        )
        self.fill(temp_color)

    #this method quickly updates a button to its basic state, meant as
    #a counterpart to hovered()
    def quickRender(self):
        self.fill(self.background_color)

    #returns a bool denoting whether or not the button is currently being hovered
    def isHovered(self, mousePOS):
        return self.get_rect(topleft = self.pos).collidepoint(mousePOS)
    #set the buttons 'clicked' status to True
    def clicked(self):
        self.is_clicked = True
        self.background_color = (183, 183, 183)

    '''if the button is clicked while hovered, it returns This buttons Label.'''
    def update(self):
        #check to see if it has been clicked
        if self.is_hovered == True:
            self.hovered()
        else:
            self.quickRender()

        if self.is_clicked == True:
            self.is_clicked = False
            return self.label

        self.blit(font.render(self.text, False, (0, 0, 0)), (self.textx, self.texty))
        return ""
