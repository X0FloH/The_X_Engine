import os
import pygame
from time import *

from Render import *

displaySize = (1000, 500)
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("X Engine V0.5 BETA Build")
display = pygame.display.set_mode(displaySize)

currentLoad = 0
loadTimes = 2
currentTime = 0
backT = False

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

    display.fill((0, 0, 0))

    back = pygame.image.load("Images/TestBack.png")
    display.blit(back, (0, 0))

    renderText((255, 255, 255), 'Sci-Fi', (275, 50), 45, "The X Engine V0.5 BETA Build", display)
    renderText((255, 255, 255), 'Sci-Fi', (470-32, 300), 35, "Loading", display)

    if currentLoad <= len(os.listdir("Images/Loading")):
        image = pygame.image.load("Images/Loading/load_" + str(currentLoad) + ".png")
        display.blit(image, (500-32, 335))
        if not backT:
            currentLoad += 1
        elif backT:
            currentLoad -= 1
    if currentLoad == len(os.listdir("Images/Loading")):
        currentLoad = len(os.listdir("Images/Loading"))-1
        backT = True
    if currentLoad == -1:
        backT = False
        currentLoad = 0
        currentTime += 1
    if currentTime == loadTimes:
        os.system('start cmd /D /C "python Startup.py && pause"')
        break

    pygame.display.update()

pygame.quit()
quit()