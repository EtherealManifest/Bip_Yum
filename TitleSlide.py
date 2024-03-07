import pygame
from pygame.locals import *
import random
import sys
import GroundMaker
import os
from pathlib import Path
import Button
import math
#FIXME: add a Back Button to return to the home screen that is always at the bottom of the screen.
# in meta, the size of the screen is recorded. Get it
META = (open('Meta.txt').read()).split(':')
WINX = int(META[0])
WINY = int(META[1])
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(20)
FPS = int(META[3])  # frames per second setting

# this is for the BIP YUM text, it will be 1/5 at high as the screen
font = pygame.font.SysFont("Planet Comic", int(WINY / 5))
NameOfTheGame = font.render("Bip Yum", False, (0, 0, 0))
GameNamePOS = (((WINX / 2) - NameOfTheGame.get_width() / 2), (WINY / 2) - NameOfTheGame.get_height() / 2)

cloudArray = []
# Cloud list, which is used to put the actual clouds in the actual sky
cloudList = os.listdir('./CloudSprites/')
for panel in cloudList:
    temp = Path('./CloudSprites/' + panel)
    cloudArray.append(pygame.image.load(temp))

cloudGroup = pygame.sprite.Group()
cloudMoveSpeed = .4
"""How fast the clouds Move"""
# number of clouds to render
cloudNum = 10
"""the number of clouds to Generate"""
# cloud move direction will be 1-8, and each will be a 45 degree clockwise angle from the last
# 1 = left
cloudMoveDirection = 1
"""the direction of the clouds. can be 1-8. each is a direction. """


# This class declares coulds and gives them a position. It has methods for
# redrawing clouds on the other side of the screen
class Cloud(pygame.sprite.Sprite):
    """One of the clouds that floats across teh title screen"""
    def __init__(self):
        """initialize the cloud sprite"""
        pygame.sprite.Sprite.__init__(self)
        # pick a random cloud sprite
        valid = False
        while not valid:
            self.image = random.choice(cloudArray)
            # define its bounding box
            self.rect = self.image.get_rect()
            valid = self.rect.width < WINX and self.rect.height < WINY
        # give it a position value that will always place it on the screen
        self.pos = [random.randrange(0, WINX - self.rect.width), random.randrange(0, WINY - self.rect.height)]
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

    def update(self):
        """Update, moving the clouds a little bit in a set direction"""
        # updating the clouds bascially involves moving them.
        # if the cloud goes off screen, remove it from the group and
        # place it on the far edge of teh screen
        if cloudMoveDirection == 1:
            self.pos[0] -= cloudMoveSpeed
            self.pos[1] += 0
        elif cloudMoveDirection == 2:
            self.pos[0] -= cloudMoveSpeed
            self.pos[1] -= cloudMoveSpeed
        elif cloudMoveDirection == 3:
            self.pos[0] -= 0
            self.pos[1] -= cloudMoveSpeed
        elif cloudMoveDirection == 4:
            self.pos[0] += cloudMoveSpeed
            self.pos[1] -= cloudMoveSpeed
        elif cloudMoveDirection == 5:
            self.pos[0] += cloudMoveSpeed
            self.pos[1] += 0
        elif cloudMoveDirection == 6:
            self.pos[0] += cloudMoveSpeed
            self.pos[1] += cloudMoveSpeed
        elif cloudMoveDirection == 7:
            self.pos[0] -= 0
            self.pos[1] += cloudMoveSpeed
        elif cloudMoveDirection == 8:
            self.pos[0] -= cloudMoveSpeed
            self.pos[1] += cloudMoveSpeed
        # if the cloud is completely off screen, set it to a random height and
        # scroll it from the other side
        if (self.pos[0] < -self.rect.width - 60):
            self.pos[0], self.pos[1] = (WINX, (random.randint(0, WINY)))
        # now update the blitting location
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]


def setTheSkies():
    """generate a bunch of random clouds to fill the skies. """
    for i in range(0, cloudNum + 1):
        newCloud = Cloud()
        cloudGroup.add(newCloud)


def changeTheSkies(currClouds):
    """if the clouds are off screen, destroy them and move them to teh other side. """
    for cloud in currClouds:
        if cloud.pos[0] < -cloud.rect.width:
            cloud = Cloud()


# returns a list of rows, each holding a list of  buttons centered in a menu that is centered on the screen.
# It bases the position of the buttons on the current number of created scenarios, specifically the number in
# ANTHOLOGY.ANTHOLOGY. To prevent a scenario from appearing in the menu, remove it from there.
def set_buttons_scenarios():
    """This is for the menu. Algorithmically generate a balanced,
    centered menu based on the number of Scenarios. Then returns the list of buttons"""
    # menu width is the maximum width the menu can occupy
    menu_width = WINX * (7 / 8)
    # menu width is the maximum height the menu can occupy
    menu_height = WINY * (7 / 8)
    # where the menu is positioned on screen
    menu_pos = [(WINX / 8) / 2, (WINY / 8) / 2]  # Center the menu window
    # a constiner for the buttons, an array of all of them
    button_grid = []
    """All of the buttons, all stored in an array"""
    # a variable that holds the accumulated value of all the buttons
    total_width = 0
    """The total width of the buttons if laid end-to-end"""
    # the list of buttons
    button_list = []
    """A list of all of the buttons"""
    # create buttons for Every Scenario
    from Anthology import ANTHOLOGY
    for scenario in ANTHOLOGY:
        # create a button, then add to the button list.
        newButton = Button.Button()
        name_length = len(scenario.name)
        """The length of this scenario's name"""
        new_width = (name_length * 7)
        """Length of the button is relative to the name"""
        newButton.modify(_pos=(0, 0), _text=scenario.name,
                         _label=scenario.name, _width=new_width)
        button_list.append(newButton)
    # determine the number of rows and add the buttons to the Button Grid
    # find the total length of all the buttons together
    for button in button_list:
        total_width += button.width
    # Now total width should equal the total width of all the buttons put together.
    # if the total width is greater than the maximum allowed width, there need to be multiple rows.
    if total_width > menu_width:
        num_rows = math.ceil(total_width / menu_width)
    else:
        num_rows = 1
    # take the value found above and divide the buttons into num_rows groups

    # make the button grid the size of the number of rows needed
    for i in range(0, num_rows):
        # add needed blank rows to the grid
        button_grid.append([])
    # divide the pool of buttons into "equal" groups based on the number of rows
    buttons_per_row = math.ceil(len(button_list) / num_rows)
    row = 0
    i = 0
    for button in button_list:
        # go through all of the buttons, adding them one row at a time.
        if i < buttons_per_row:
            button_grid[row].append(button)
            i += 1
        else:
            row += 1
            i = 0
            button_grid[row].append(button)
    # at this point, all the buttons have been added, and are sorted into groups.
    # now, the buttons need to be formatted.
    # for each row, balance all of the buttons. First set the width.
    # The default dimensions for a button are 20pxh x 100pxw

    i = 0
    # for each row in button grid
    for i in range(0, len(button_grid)):
        # determine the position of each button
        # for each button in this row
        # currently referenced button in this row
        index = 0
        # set the x-position for this row
        # the average space between each button in this row
        spacing_constant = menu_width / (len(button_grid[i]) +1) + 5
        for button in button_grid[i]:
            #this looks dumb, and it kinda is. Its a massive coordinate tuple
            button_grid[i][index].pos = (menu_pos[0] + ((spacing_constant * (index + 1)) - ((1 / 2) * button.width)), 0)
            index += 1
    # now, the x-positions for all of the buttons should be set

    # set the y positions
    for i in range(0, len(button_grid)):
        # determine the position of each button
        # for each button in this row
        # currently referenced button in this row
        index = 0
        # set the x-position for this row
        # the average space between each button in this row
        spacing_constant = menu_height / (len(button_grid) + 1)
        for button in button_grid[i]:
            #this looks stupid, it's a massive tuple so that it can be assigned to pos.
            #it takes the current X value and midifies the Y
            button_grid[i][index].pos = (button_grid[i][index].pos[0], menu_pos[1] + ((spacing_constant * (i + 1)) -
                                                                                      ((1 / 2) * button.height)))
            index += 1
    # now each button should be in the correct Y position.
    # add listeners to each button that will return the scenario that they point to back to the
    # game.py to run the scenario.
    '''this is handled outside of here. See documentation for Button.update()'''
    return button_grid


# this is the loop that runs the title screen
def runTitle(DISPLAYSURF):
    """Run the title screen.

    If no buttons are pressed, return nothing. Otherwise, return a string:
    The label of the button pressed."""
    # Program Start:
    openSky = pygame.Surface((WINX, WINY))
    openSky.fill((25, 186, 255))
    setTheSkies()
    # I want to be able to scale the clouds. in order to do that, they need to
    # be surfaces, not sprites. I'm gonna add an intermediary that converts them
    # to a surface, then blits the surfaces together.
    cloudGroup.draw(openSky)
    DISPLAYSURF.blit(openSky, (0, 0))
    Grass = GroundMaker.PlantTheGrass(WINX, WINY)
    # buttons
    button_list = []
    start_button = Button.Button()
    quit_button = Button.Button()
    start_button.modify(_pos=(WINX / 2 - start_button.get_rect().width / 2, 2 * WINY / 3), _text="START",
                        _label="start-button")
    button_list.append(start_button)
    quit_button.modify(_pos=(start_button.pos[0],
                             start_button.pos[1] + 2 * start_button.height),
                       _text="QUIT",
                       _label='quit-button')
    button_list.append(quit_button)

    # load the scenario menu
    scenario_menu_list = set_buttons_scenarios()

    # title Text
    while True:
        changeTheSkies(cloudGroup)
        cloudGroup.update()
        # when the user makes a selection, return the selection to Game.py
        openSky.fill((25, 186, 255))
        cloudGroup.draw(openSky)
        Grass.draw(openSky)
        DISPLAYSURF.blit(openSky, (0, 0))
        # blit the text onto the screen
        DISPLAYSURF.blit(NameOfTheGame, GameNamePOS)
        # Load the button
        for button in button_list:
            DISPLAYSURF.blit(button, button.pos)
            button.is_hovered = False

            # before I get here, if start has been selected, the button list needs to be changed to show all available
        # scenarios.
        # check to see if the mouse is positioned over the start button
        for button in button_list:
            if (button.isHovered(pygame.mouse.get_pos())):
                # set the cursor to a focused cursor
                button.is_hovered = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                # if the left button is clicked
                if (pygame.mouse.get_pressed()[0]):
                    button.is_clicked = True
            status = button.update()

            if status == 'start-button':
                # enter another While True loop. This time for the scenario buttons.
                # this will be escaped either by selecting a scenario (return scenario code) or
                # by pressing back to come back to this menu (break)
                while True:
                    changeTheSkies(cloudGroup)
                    cloudGroup.update()
                    # when the user makes a selection, return the selection to Game.py
                    openSky.fill((25, 186, 255))
                    cloudGroup.draw(openSky)
                    DISPLAYSURF.blit(openSky, (0, 0))
                    for row in scenario_menu_list:
                        for button in row:
                            DISPLAYSURF.blit(button, button.pos)
                            button.is_hovered = False
                    # check to see if the mouse is positioned over any button
                    for row in scenario_menu_list:
                        for button in row:
                            if (button.isHovered(pygame.mouse.get_pos())):
                                # set the cursor to a focused cursor
                                button.is_hovered = True
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                # if the left button is clicked
                                if (pygame.mouse.get_pressed()[0]):
                                    button.is_clicked = True
                            status = button.update()
                            if status != "":
                                print(status + " scenario selected")
                                #return all the way to game.py
                                return status

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            return 'Q'

                    pygame.display.update()
                    fpsClock.tick(FPS)

            if status != "":
                #return all the way to game.py
                return status

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'Q'

        pygame.display.update()
        fpsClock.tick(FPS)
