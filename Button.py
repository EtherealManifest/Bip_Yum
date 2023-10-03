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
        self.pos = _pos
        self.background_color = _background_color
        self.fill(self.background_color)
        self.label = _label
        global font
        font = pygame.font.SysFont("System", self.height)

        buttonText = font.render(self.text, False, (0, 0, 0))
        self.textx = (self.width / 2 - buttonText.get_width()/2)
        print("Width: " + str(self.width) + ", height: " + str(self.height))
        print("Size required to hold text: " + str(font.size(self.text)))
        self.texty = (self.height / 2 - buttonText.get_height()/2)
        self.blit(buttonText, (self.textx, self.texty))
        self.is_clicked = False
        self.is_hovered = False

    def hovered(self):
        temp_color =(
            self.background_color[0] - 50,
            self.background_color[1] - 50,
            self.background_color[2] - 50
        )
        self.fill(temp_color)

    def isHovered(self, mousePOS):
        return self.get_rect(topleft = self.pos).collidepoint(mousePOS)

    def clicked(self):
        self.is_clicked = True
        self.background_color = (183, 183, 183)

    def update(self):
        #check to see if it has been clicked
        if self.is_hovered == True:
            self.hovered()
        if self.is_clicked == True:
            self.is_clicked = False;
            return self.label
        self.blit(font.render(self.text, False, (0, 0, 0)), (self.textx, self.texty))
        return ""
