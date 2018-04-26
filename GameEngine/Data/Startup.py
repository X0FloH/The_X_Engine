import pygame
import shutil
import os
from time import *
import webbrowser

hasClip = True
try:
    import pyperclip
except:
    hasClip = False

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

copyClipPos = [1100, 850]
showClip = False

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

#Load the logo
logo = pygame.image.load('Images/Logo/32bit.png')
pygame.display.set_icon(logo)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
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

    #The about page
    if selectedTab == 1:
        renderText((255, 255, 255), 'Ariel', (100, 700), 30, 'Contact:', display)
        renderText((184, 0, 149), 'Ariel', (190, 700), 30, 'xengine.contact@gmail.com', display)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 190, 700, 300, 25) and hasClip:
            pyperclip.copy('xengine.contact@gmail.com')
            showClip = True
        renderText((255, 255, 255), 'Ariel', (100, 750), 30, 'Report Bugs:', display)
        renderText((184, 0, 149), 'Ariel', (240, 750), 30, 'xengine.bugs@gmail.com', display)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 240, 750, 300, 25) and hasClip:
            pyperclip.copy('xengine.bugs@gmail.com')
            showClip = True

        twitter = pygame.image.load('Images/Social/twitter.png').convert_alpha()
        display.blit(twitter, (700, 700))
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 700, 700, 64, 64):
            webbrowser.open('https://twitter.com/X0FloH')
        if hoveredRect(mousePos[0], mousePos[1], 700, 700, 64, 64):
            renderText((0, 0, 255), 'Ariel', (700, 764), 20, "@X0FloH", display)
            
        renderText((255, 255, 255), 'Ariel', (100, 150), 35, "The X Engine was created by an 11 year-old indie game developer.", display)
        renderText((255, 255, 255), 'Ariel', (100, 190), 35, "I was creating a game for the YGBs (Young Game Baftas) and I created a physics engine for my game.", display)
        renderText((255, 255, 255), 'Ariel', (100, 230), 35, "this made me think about how engines like Unity an Unreal Engine 4 had their own physics engine", display)
        renderText((255, 255, 255), 'Ariel', (100, 270), 35, "and I decided to make my own.", display)
        renderText((255, 255, 255), 'Ariel', (100, 350), 35, "I knew how to do basic pygame things in python and so I designed a 2D engine", display)
        renderText((255, 255, 255), 'Ariel', (100, 390), 35, "which had visual scripting and when you exported the game it made it into a python file.", display)

        me = pygame.image.load('Images/me.png')
        display.blit(me, ((displaySize[0]/2)-128, 430))

        renderText((255, 0, 37), 'Ariel', ((displaySize[0]/2)-128-40, 430+171+10), 25, "Oscar Jones - Developer", display)
        
    if (selectedGame >= 0 and selectedTab == 0):
        image = pygame.image.load('Images/Arrow.png')
        display.blit(image, (displaySize[0]-130, displaySize[1]-74))
        keys = pygame.key.get_pressed()
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, displaySize[0]-130, displaySize[1]-74, 130, 74) or keys[pygame.K_RETURN]:
            writeFile("Saves/" + displayGames()[selectedGame] + "/using.txt", "True", "w")
            os.system('start cmd /D /C "python Engine.py && pause"')
            file = open("Engine.py", "r+")
            exec(file.read())
            running = False
        renderText((255, 0, 255), 'Ariel', (100, 500), 40, "Description", display)
        renderText((255, 255, 255), 'Ariel', (100,550), 35, readFile("Saves/" + displayGames()[selectedGame] + "/desc.txt", "File"), display)

    if selectedTab == 0 and mouseClicked and oldGame == selectedGame:
        selectedGame = -1
        oldGame = -1

    for event in events:
        if event.type == pygame.KEYDOWN:
            if selectedTab == 0 and selectedGame >= 0 and event.key == pygame.K_DELETE:
                ask = True
                while ask:
                    renderText((255, 0, 0), 'Ariel', (300, 450), 60, "Are you sure you want to delete this? (y/n)",display)
                    pygame.display.update()
                    events2 = pygame.event.get()
                    for event2 in events2:
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_y:
                                shutil.rmtree("Saves/" + displayGames()[selectedGame])
                                selectedGame = -1
                                ask = False
                            if event2.key == pygame.K_n:
                                ask = False
            if selectedTab == 2 and selectedInput == 0 and event.key == pygame.K_TAB:
                selectedInput = 1
            elif selectedTab == 2 and selectedInput == 1 and event.key == pygame.K_TAB:
                selectedInput = 0

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
        inputs[0] = inputs[0][:12]
        renderText((255, 255, 255), 'Ariel', (100, 250), 35, inputs[0], display)
        renderText((255, 255, 255), 'Ariel', (300, 250), 25, str(12-len(inputs[0])), display)
        renderText((255, 255, 255), 'Ariel', (100, 450), 35, inputs[1], display)

        if os.path.exists("Saves/" + inputs[0]) and not inputs[0] == "":
            renderText((255, 0, 0), 'Ariel', (300, 200), 35, "There is already a file named this.", display)

        if not inputs[0] == "" and not os.path.exists("Saves/" + inputs[0]):
            tick = pygame.image.load("Images/Tick.png")
            display.blit(tick, (210, 200))
        if not inputs[1] == "":
            tick = pygame.image.load("Images/Tick.png")
            display.blit(tick, (305, 400))

        if not inputs[0] == "" and not inputs[1] == "" and not os.path.exists("Saves/" + inputs[0]):
            image = pygame.image.load('Images/Arrow.png')
            display.blit(image, (displaySize[0]-130, displaySize[1]-74))
            for event in events:
                if clickedRect(mousePos[0], mousePos[1], mouseClicked, displaySize[0]-130, displaySize[1]-74, 130, 74) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                    os.makedirs("Saves/" + inputs[0])
                    os.makedirs("Saves/" + inputs[0] + "/Objects")
                    writeFile("Saves/" + inputs[0] + "/desc.txt", inputs[1])
                    writeFile("Saves/" + inputs[0] + "/using.txt", "False")
                    selectedTab = 0
                    selectedGame = getIndex(inputs[0], displayGames())
                    inputs[0] = ""
                    inputs[1] = ""

    if showClip:
        newDisp = pygame.Surface((350, 50)).convert_alpha()
        newDisp.fill((0, 0, 0, 0), None, pygame.BLEND_RGBA_MULT)
        renderText((0, 0, 255), 'Ariel', (0, 0), 35, 'Copied To Clip Board', newDisp)
        display.blit(newDisp, (copyClipPos[0], copyClipPos[1]))
        if copyClipPos[1] < 35:
            copyClipPos[1] = 850
            showClip = False
        copyClipPos[1] -= 1.5


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
