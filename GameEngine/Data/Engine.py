import pygame
import shutil
import os
import random
from time import *
import webbrowser

#Import all the scripts
from Render import *
from UserInput import *
from Data import *
from Sensing import *

#Find the one we are using
using = ""
for game in displayGames():
    if readFile("Saves/" + game + "/using.txt", "File") == "True":
        using = game
        #Avoid confusion
        writeFile("Saves/" + game + "/using.txt", "False", "w")

#Camera variables
editX = 0
editY = 0
editMSPos = [0, 0]

#Engine variables
gameSpeed = 1

#The mouse variables
mouseDown = False
mouseRightDown = False
mouseRightClicked = False
mouseRightHasClicked = False
mouseClicked = False
mouseHasClicked = False

#Some default variables
backgroundCol = (0, 0, 0)

surface = pygame.display.get_surface()
displaySize = (1000, 700)

#Some menu variables
createMenu = False

currentAction = 0

#Object variables
clickedObject = False
doingAction = False
selectedObject = "square3.txt"

#Action Variables
moveMSPos = [0, 0]
selectedXMove = False

#Setup Pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("X Engine 0.5 - " + using)
display = pygame.display.set_mode(displaySize)

#Load the logo
logo = pygame.image.load('Images/Logo/32bit.png')
pygame.display.set_icon(logo)

#Start the loop
running = True
while running and not using == "":
    #Add the delay
    sleep(magInverse(gameSpeed))

    #Check for quiting
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                doIt = True
                while doIt:
                    display.fill((0,0,0))
                    renderText((255, 0, 0), 'Ariel', (700, 450), 55, "Quit", display)
                    events2 = pygame.event.get()
                    for event2 in events2:
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_RETURN:
                                running = False
                                doIt=False
                            if event2.key == pygame.K_ESCAPE:
                                doIt = False
                    pygame.display.update()

    #Mouse Setup
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
    if mouseRightDown and mouseRightHasClicked and mouseRightClicked:
        mouseRightClicked = False
    if mouseRightDown and not mouseRightHasClicked:
        mouseRightClicked = True
        mouseRightHasClicked = True
    if not mouseRightDown:
        mouseRightClicked = False
        mouseRightHasClicked = False

    #Empty the screen
    display.fill((0, 0, 0))

    #Draw all the objects
    objectsPlace = pygame.Surface((displaySize[0]-350, displaySize[1]-80))
    for obj in os.listdir("Saves/" + using + "/Objects"):
        if readFile("Saves/" + using + "/Objects/" + obj)[0] == "square\n":
            if inWindow(displaySize[0]-350, displaySize[1]-80, int(readFile("Saves/" + using + "/Objects/" + obj)[4])+editX,  int(readFile("Saves/" + using + "/Objects/" + obj)[5])+editY, int(readFile("Saves/" + using + "/Objects/" + obj)[6]), int(readFile("Saves/" + using + "/Objects/" + obj)[7])):
                if obj == selectedObject:
                    renderRect((255, 140,0), (int(readFile("Saves/" + using + "/Objects/" + obj)[4])-5+editX,int(readFile("Saves/" + using + "/Objects/" + obj)[5])-5+editY), (int(readFile("Saves/" + using + "/Objects/" + obj)[6])+10,int(readFile("Saves/" + using + "/Objects/" + obj)[7])+10),objectsPlace)

                renderRect((int(readFile("Saves/" + using + "/Objects/" + obj)[1]),int(readFile("Saves/" + using + "/Objects/" + obj)[2]),int(readFile("Saves/" + using + "/Objects/" + obj)[3])), (int(readFile("Saves/" + using + "/Objects/" + obj)[4])+editX,int(readFile("Saves/" + using + "/Objects/" + obj)[5])+editY), (int(readFile("Saves/" + using + "/Objects/" + obj)[6]),int(readFile("Saves/" + using + "/Objects/" + obj)[7])), objectsPlace)

                if currentAction == 0 and selectedObject == obj:
                    renderRect((0, 0, 255), (int(readFile("Saves/" + using + "/Objects/" + obj)[4])+editX+(int(int(readFile("Saves/" + using + "/Objects/" + obj)[6])/2)), (int(readFile("Saves/" + using + "/Objects/" + obj)[5])+editY-10+(int(int(readFile("Saves/" + using + "/Objects/" + obj)[7])/2)))), (int(readFile("Saves/" + using + "/Objects/" + obj)[6])*2, 20), objectsPlace)
                    if (mouseDown and hoveredRect(mousePos[0], mousePos[1], int(readFile("Saves/" + using + "/Objects/" + obj)[4])+editX+(int(int(readFile("Saves/" + using + "/Objects/" + obj)[6])/2)), int(readFile("Saves/" + using + "/Objects/" + obj)[5])+editY+(int(int(readFile("Saves/" + using + "/Objects/" + obj)[7]))/2), int(readFile("Saves/" + using + "/Objects/" + obj)[6])*2, 20)) or selectedXMove:
                        doingAction = True
                        if mouseClicked:
                            moveMSPos[0] = mousePos[0]
                            moveMSPos[1] = mousePos[1]
                        writeFileLines("Saves/"+ using + "/Objects/" + obj, str(int(readFile("Saves/" + using + "/Objects/" + obj)[4]) + mousePos[0]-moveMSPos[0]), 4)
                        moveMSPos[0] = mousePos[0]
                        moveMSPos[1] = mousePos[1]
                        selectedXMove = True
                    else:
                        doingAction = False

                if clickedRect(mousePos[0], mousePos[1]-80, mouseClicked, int(readFile("Saves/" + using + "/Objects/" + obj)[4])+editX, int(readFile("Saves/" + using + "/Objects/" + obj)[5])+editY, int(readFile("Saves/" + using + "/Objects/" + obj)[6]), int(readFile("Saves/" + using + "/Objects/" + obj)[7])):
                    selectedObject = obj
                    clickedObject = True

        if readFile("Saves/" + using + "/Objects/" + obj)[0] == "circle\n":
            renderCircle((int(readFile("Saves/" + using + "/Objects/" + obj)[1]),int(readFile("Saves/" + using + "/Objects/" + obj)[2]),int(readFile("Saves/" + using + "/Objects/" + obj)[3])), (int(readFile("Saves/" + using + "/Objects/" + obj)[4]),int(readFile("Saves/" + using + "/Objects/" + obj)[5])), int(readFile("Saves/" + using + "/Objects/" + obj)[6]), objectsPlace)
        
    


    #Empty selection
    if mouseClicked and not clickedObject and not doingAction:
        selectedObject = ""
    clickedObject = False

    #Stop X Moving
    if selectedXMove and mouseDown == False:
        selectedXMove = False

    #Render the objectsPlace
    display.blit(objectsPlace, (0, 80))

    #Draw the Icons
    iconPlace = pygame.Surface((displaySize[0]-350, 80))
    iconPlace.fill((91,91,91))
    new = pygame.image.load('Images/Icons/NewIcon.png').convert_alpha()
    if hoveredRect(mousePos[0], mousePos[1], 60, 20, 32, 32):
        renderText((0, 255, 0), 'Ariel', (50, 56), 25, "Create", iconPlace)
    if clickedRect(mousePos[0], mousePos[1], mouseClicked, 60, 20, 32, 32):
        createMenu = True
    iconPlace.blit(new, (60, 20))
    #Draw the Actions
    position = pygame.image.load("Images/Icons/Actions/PosArrows.png")
    if clickedRect(mousePos[0], mousePos[1], mouseClicked, displaySize[0]-350-(36*3)-10, 20, 32, 32):
        currentAction = 0
    iconPlace.blit(position, (displaySize[0]-350-(36*3)-10, 20))

    #Draw the inspector panel
    inspector = pygame.Surface((350, displaySize[1]))
    inspector.fill((70, 70, 70))

    #Render the inspector panel
    display.blit(inspector, (displaySize[0]-350, 0))

    #Render the IconPlace
    display.blit(iconPlace, (0, 0))

    #Draw the create menu
    if createMenu:
        if not hoveredRect(mousePos[0], mousePos[1], 60, 20, 150, 200+32+20):
            createMenu = False
        menuPlace = pygame.Surface((150, 200))
        menuPlace.fill((74, 74, 74))
        square = pygame.image.load('Images/Icons/Create/Square.png')
        renderText((255, 0, 0), 'Ariel', (30 + 32 + 20, (30 + (32/2))-(25/2)), 25, "Square", menuPlace)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 0, 20+32+20, 150, 75):
            writeFile("Saves/" + using + "/Objects/square" + str(len(os.listdir("Saves/" + using + "/Objects"))+1) + ".txt", "square\n255\n255\n255\n" + str(random.randrange(0, displaySize[0]-350)-editX) + "\n" + str(random.randrange(0, displaySize[1]-80)-editY) + "\n50\n50", "w")
        menuPlace.blit(square, (30, 30))
        renderRect((60, 60, 60), (0, 75), (150, 10), menuPlace)
        square = pygame.image.load('Images/Icons/Create/Circle.png')
        renderText((255, 0, 0), 'Ariel', (30 + 32 + 20, (100 + (32/2))-(25/2)), 25, "Circle", menuPlace)
        if clickedRect(mousePos[0], mousePos[1], mouseClicked, 0, 20+32+20+85, 150, 115):
            writeFile("Saves/" + using + "/Objects/circle" + str(len(os.listdir("Saves/" + using + "/Objects"))+1) + ".txt", "circle\n255\n255\n255\n" + str(random.randrange(0, displaySize[0]-350)-editX) + "\n" + str(random.randrange(0, displaySize[1]-80)-editY) + "\n50\n50", "w")
        menuPlace.blit(square, (30, 100))
        display.blit(menuPlace, (60, 20+32+20))

    #Delete the selected object when Del or backspace is clicked
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                if not selectedObject == "":
                    os.remove("Saves/" + using + "/Objects/" + selectedObject)

    #Drag the editorCam
    if mouseRightDown and not createMenu:
        if mouseRightClicked:
            editMSPos[0] = mousePos[0]
            editMSPos[1] = mousePos[1]
        editX += mousePos[0]-editMSPos[0]
        editY += mousePos[1]-editMSPos[1]
        editMSPos[0] = mousePos[0]
        editMSPos[1] = mousePos[1]

    
        
 
    #Refresh the screen
    pygame.display.update()

#Then, quit
pygame.quit()
quit()




        
