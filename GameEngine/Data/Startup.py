import pygame
import os
from time import *

#Import all the scripts
from Render import *
from UserInput import *
from Data import *

#Declare the variables
backgroundCol = (0, 0, 0)
displaySize = (1500, 900)
mouseDown = False
mouseRightDown = False
mouseClicked = False
mouseHasClicked = False
running = True

selectedTab = 0

#Declare the lists
tabs = [["Create", 100, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel'], ["About", 300, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel']]

#Setup Pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("X Engine Launcher 0.5")
display = pygame.display.set_mode(displaySize)

#Main Loop
while running:
    #Quit stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    #Clear the screen
    display.fill(backgroundCol)

    #Mouse stuff
    mousePos = pygame.mouse.get_pos()
    mouseClkData = pygame.mouse.get_pressed()
    mouseDown = bool(mouseClkData[0])
    mouseRightDown = bool(mouseClkData[2])
    if mouseDown and mouseHasClicked and mouseClicked:
        mouseClicked = False
    if mouseDown and not mouseHasClicked:
        mouseClicked = True
        mouseHasClicked = True
    if not mouseDown:
        mouseClicked = False
        mouseHasClicked = False

    #Draw the tabs
    for tab in tabs:
        renderText(tab[6], tab[8], (tab[1], tab[2]), tab[7], tab[0], display)
        if tab[5][0]:
            renderRect(tab[5][1], (tab[1], tab[2]), (tab[3], tab[4]), display)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, tab[1], tab[2], (tab[3]), (tab[4]/2)):
            selectedTab = getIndex(tab, tabs)
        if selectedTab == getIndex(tab, tabs):
            renderRect((255, 255, 255), (tab[1], tab[2] + 40), (tab[3], 3), display)

    if selectedTab == 0:
        renderText((255, 255, 255), 'Ariel', (200, 150), 50, 'Games', display)
        games = displayGames()
        i = 1
        while i-1 < len(games):
             renderRect((255, 0, 0), (i * 120, 300), (100, 100), display)
             i = i + 1
    
    pygame.display.update()

#Quit
pygame.quit()
quit()
