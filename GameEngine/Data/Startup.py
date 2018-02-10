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
currentInput = ""

selectedTab = 0
selectedGame = -1
oldGame = -1

#Declare the lists
tabs = [["Open", 100, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel'], ["About", 300, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel'], ["Create", 500, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel']]
folders = ["Saves"]

#Setup Folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

#Setup Pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("X Engine Launcher 0.5")
display = pygame.display.set_mode(displaySize)

#To not worry about sleep
def wait(time):
    sleep(time)
    return

#Main Loop
while running:
    #Quit stuff
    events = pygame.event.get()
    for event in events:
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
        renderText((255, 255, 255), 'Ariel', (100, 150), 50, 'Your Games', display)
        games = displayGames()
        i = 1
        while i-1 < len(games):
            if not selectedGame == i-1:
                renderRect((255, 0, 0), ((i * 190)-100, 200), (150, 200), display)
                renderText((71, 212, 100), 'Ariel', ((i * 190)-100, 420), 35, games[i-1], display)
            else:
                renderRect((255, 50, 0), ((i * 190)-100, 200), (150, 200), display)
                renderText((94, 255, 34), 'Ariel', ((i * 190)-100, 420), 35, games[i-1], display)

            if clickedRect(mousePos[0], mousePos[1], mouseClicked, (i *190)-100, 200, 150, 200):
                selectedGame = i-1
            i = i + 1

    if selectedGame >= 0 and selectedTab == 0:
        image = pygame.image.load('Images/Arrow.png')
        display.blit(image, (displaySize[0]-130, displaySize[1]-74))

    if selectedTab == 0 and mouseClicked and oldGame == selectedGame:
        selectedGame = -1
        oldGame = -1

    oldGame = selectedGame

    currentInput = inputField(events, currentInput)

    renderText((94, 255, 34), 'Ariel', ((i * 190)-100, 420), 35, currentInput, display)
    
    pygame.display.update()

#To open a seperate file
#os.system('start cmd /D /C "python Test.py && pause"')

#Quit
pygame.quit()
quit()
