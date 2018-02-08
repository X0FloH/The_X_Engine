import pygame
import os
from time import *
import pyperclip

displaySize = (1000, 900)
backgroundColor = (0, 0, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

mouseDown = False

pygame.display.set_caption("Project Falcon Level Designer")
display = pygame.display.set_mode(displaySize)

minSliderVal = 200
maxSliderVal = int((minSliderVal + 510))

sliders = [[maxSliderVal, 550, 50, 25, (255, 0, 0)], [maxSliderVal, 600, 50, 25, (0, 255, 0)], [maxSliderVal, 650, 50, 25, (0, 0, 255)]]

heldObjIndex = -1
selectedSliderIndex = -1

currentColor = [255, 255, 255]

def drawSquare(xPos, yPos, xSize, ySize, color):
    obst = pygame.draw.rect(display, color, pygame.Rect(xPos, yPos, xSize, ySize))
    return obst

def drag(currentX, currentY, xSize, ySize, newX, newY):
    currentX = newX - (xSize/2)
    currentY = newY - (ySize/2)
    return currentX, currentY

def sliderDrag(currentX, xSize, mouseX):
    currentX = mouseX - (xSize/2)
    return currentX

def getIndex(find, listS):
    foundIndex = -1
    i = 0
    while i < len(listS):
        if find == listS[i]:
            foundIndex = i
        i = i + 1
    return foundIndex

def wait(time):
    sleep(time)
    return

running = True
changingColor = True

colorCircleRadius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if pygame.mouse.get_pressed()[0]:
        mouseDown = True
    else:
        mouseDown = False

    if pygame.mouse.get_pressed()[1]:
        mouseDownRight = True
    else:
        mouseDownRight = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p] or keys[pygame.K_RETURN]:
        string = "(" + str(currentColor[0]) + ", " + str(currentColor[1]) + ", " + str(currentColor[2]) + ")"
        pyperclip.copy(string)

        wait(.1)
        
    currentColor[0] = int((sliders[0][0] - minSliderVal)/2)
    currentColor[1] = int((sliders[1][0] - minSliderVal)/2)
    currentColor[2] = int((sliders[2][0] - minSliderVal)/2)

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    display.fill(backgroundColor)
    colorBlock = pygame.draw.circle(display, (currentColor[0], currentColor[1], currentColor[2]), (int(displaySize[0]/2), int(displaySize[1]/2) - 200), colorCircleRadius * 6)

    for slider in sliders:
        slid = drawSquare(slider[0], slider[1], slider[2], slider[3], slider[4])
        if mouseDown and mouseX > slider[0] and mouseX < slider[0] + slider[2] and mouseY > slider[1] and mouseY < slider[1] + slider[3]:
            selectedSliderIndex = getIndex(slider, sliders)
        elif mouseDown == False:
            selectedSliderIndex = -1

        if selectedSliderIndex == getIndex(slider, sliders):
            slider[0] = sliderDrag(slider[0], slider[2], mouseX)
            
            if slider[0] < minSliderVal:
                slider[0] = minSliderVal
            if slider[0] > maxSliderVal:
                slider[0] = maxSliderVal


    pygame.display.update()

pygame.quit()
quit()
