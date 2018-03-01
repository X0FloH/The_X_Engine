import pygame
import shutil
import os
from time import *
import webbrowser

#Import all the scripts
from Render import *
from UserInput import *
from Data import *

#Find the one we are using
using = ""
for game in displayGames():
    if readFile("Saves/" + game + "/using.txt", "File") == "True":
        using = game

#The mouse variables
mouseDown = False
mouseRightDown = False
mouseClicked = False
mouseHasClicked = False

#Some default variables
backgroundCol = (0, 0, 0)
displaySize = (1500, 900)

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
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                doIt = True
                while doIt:
                    renderText((255, 0, 0), 'Ariel', (700, 450), 55, "Quit", display)
                    events2 = pygame.event.get()
                    for event2 in events2:
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_RETURN:
                                running = False
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

    #Empty the screen
    display.fill((0, 0, 0))

    #Draw the Icons
    iconPlace = pygame.Surface((1500, 80))
    iconPlace.fill((91,91,91))
    new = pygame.image.load('Images/Icons/NewIcon.png').convert_alpha()
    if hoveredRect(mousePos[0], mousePos[1], 60, 20, 32, 32):
        renderText((0, 255, 0), 'Ariel', (50, 56), 25, "Create", iconPlace)
    iconPlace.blit(new, (60, 20))

    #Render the IconPlace
    display.blit(iconPlace, (0, 0))
 
    #Refresh the screen
    pygame.display.update()
    
#Stop using the game
writeFile("Saves/" + game + "/using.txt", "False", "w")

#Then, quit
pygame.quit()
quit()




        
