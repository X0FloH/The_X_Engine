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

selectedInput = -1

#Declare the lists
tabs = [["Open", 100, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel'], ["About", 300, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel'], ["Create", 500, 50, 100, 100, [False, (255, 0, 0)], (231, 47, 46), 50, 'Ariel']]
folders = ["Saves"]
inputs = ["", ""]

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

    if selectedTab == 2:
        if selectedInput == 0:
            renderText((255, 84, 92), 'Ariel', (100, 200), 50, "Name", display)
        elif not selectedInput == 0:
            renderText((84, 84, 92), 'Ariel', (100, 200), 50, "Name", display)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 100, 250, 1000, 50):
            selectedInput = 0
        if selectedInput == 1:
            renderText((255, 84, 92), 'Ariel', (100, 400), 50, "Description", display)
        elif not selectedInput == 1:
            renderText((84, 84, 92),'Ariel', (100, 400), 50, "Description", display)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 100, 450, 1000, 50):
            selectedInput = 1
        if selectedInput == 0:
            inputs[0] = inputField(events, inputs[0], False)
        if selectedInput == 1:
            inputs[1] = inputField(events, inputs[1], True)
        renderText((255, 255, 255), 'Ariel', (100, 250), 35, inputs[0], display)
        renderText((255, 255, 255), 'Ariel', (100, 450), 35, inputs[1], display)

        if not inputs[0] == "":
            tick = pygame.image.load("Images/Tick.png")
            display.blit(tick, (210, 200))
        if not inputs[1] == "":
            tick = pygame.image.load("Images/Tick.png")
            display.blit(tick, (305, 400))

        if not inputs[0] == "" and not inputs[1] == "":
            image = pygame.image.load('Images/Arrow.png')
            display.blit(image, (displaySize[0]-130, displaySize[1]-74))


    oldGame = selectedGame

    #How to do inputs:
    #currentInput = inputField(events, currentInput)
    #renderText((94, 255, 34), 'Ariel', ((i * 190)-100, 420), 35, currentInput, display)
    
    pygame.display.update()

#To open a seperate file
#os.system('start cmd /D /C "python Test.py && pause"')

#Quit
pygame.quit()
quit()
