import pygame
from Data import *

def clickedRect(mouseX, mouseY, mouseClick, xPos, yPos, xSize, ySize):
    if mouseX > xPos and mouseX < xPos + xSize and mouseY > yPos and mouseY < yPos + ySize and mouseClick:
        return True
    else:
        return False

def keysPressed(events, special=True):
    pressed = []
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pressed.append("a")
            if event.key == pygame.K_b:
                pressed.append("b")
            if event.key == pygame.K_c:
                pressed.append("c")
            if event.key == pygame.K_d:
                pressed.append("d")
            if event.key == pygame.K_e:
                pressed.append("e")
            if event.key == pygame.K_f:
                pressed.append("f")
            if event.key == pygame.K_g:
                pressed.append("g")
            if event.key == pygame.K_h:
                pressed.append("h")
            if event.key == pygame.K_i:
                pressed.append("i")
            if event.key == pygame.K_j:
                pressed.append("j")
            if event.key == pygame.K_k:
                pressed.append("k")
            if event.key == pygame.K_l:
                pressed.append("l")
            if event.key == pygame.K_m:
                pressed.append("m")
            if event.key == pygame.K_n:
                pressed.append("n")
            if event.key == pygame.K_o:
                pressed.append("o")
            if event.key == pygame.K_p:
                pressed.append("p")
            if event.key == pygame.K_q:
                pressed.append("q")
            if event.key == pygame.K_r:
                pressed.append("r")
            if event.key == pygame.K_s:
                pressed.append("s")
            if event.key == pygame.K_t:
                pressed.append("t")
            if event.key == pygame.K_u:
                pressed.append("u")
            if event.key == pygame.K_v:
                pressed.append("v")
            if event.key == pygame.K_w:
                pressed.append("w")
            if event.key == pygame.K_x:
                pressed.append("x")
            if event.key == pygame.K_y:
                pressed.append("y")
            if event.key == pygame.K_z:
                pressed.append("z")
            if event.key == pygame.K_0:
                pressed.append("0")
            if event.key == pygame.K_1:
                pressed.append("1")
            if event.key == pygame.K_2:
                pressed.append("2")
            if event.key == pygame.K_3:
                pressed.append("3")
            if event.key == pygame.K_4:
                pressed.append("4")
            if event.key == pygame.K_5:
                pressed.append("5")
            if event.key == pygame.K_6:
                pressed.append("6")
            if event.key == pygame.K_7:
                pressed.append("7")
            if event.key == pygame.K_8:
                pressed.append("8")
            if event.key == pygame.K_9:
                pressed.append("9")

            #For the special characters
            if special:
                if event.key == pygame.K_SPACE:
                    pressed.append(" ")
                if event.key == pygame.K_COMMA:
                    pressed.append(",")
                if event.key == pygame.K_PERIOD:
                    pressed.append(".")

            #For the modifiers
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                pressed.append("Shift")
            if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                pressed.append("Ctrl")
            if keys[pygame.K_LALT] or keys[pygame.K_RALT]:
                pressed.append("Alt")
            if keys[pygame.K_BACKSPACE]:
                pressed.append("Del")

            if special:
                if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                    if event.key == pygame.K_1:
                        pressed.append("!")
                        del pressed[getIndex("1", pressed)]
                    if event.key == pygame.K_2:
                        pressed.append('"')
                        del pressed[getIndex("2", pressed)]
                    if event.key == pygame.K_3:
                        pressed.append("£")
                        del pressed[getIndex("3", pressed)]
                    if event.key == pygame.K_4:
                        pressed.append("$")
                        del pressed[getIndex("4", pressed)]
                    if event.key == pygame.K_5:
                        pressed.append("%")
                        del pressed[getIndex("5", pressed)]
                    if event.key == pygame.K_6:
                        pressed.append("^")
                        del pressed[getIndex("6", pressed)]
                    if event.key == pygame.K_7:
                        pressed.append("&")
                        del pressed[getIndex("7", pressed)]
                    if event.key == pygame.K_8:
                        pressed.append("*")
                        del pressed[getIndex("8", pressed)]
                    if event.key == pygame.K_9:
                        pressed.append("(")
                        del pressed[getIndex("9", pressed)]
                    if event.key == pygame.K_0:
                        pressed.append(")")
                        del pressed[getIndex("0", pressed)]
                        
                
    return pressed

def inputField(events, current, special=True):
    for key in keysPressed(events):
        if not contains("Ctrl", keysPressed(events, special)) and not contains("Shift", keysPressed(events, special)) and not contains("Alt", keysPressed(events, special)) and not contains("Del", keysPressed(events, special)):
            current += key
        if contains("Shift", keysPressed(events, special)):
            if not key == "Shift" and not key == "Alt" and not key == "Ctrl" and not key == "Del":
                current += key.upper()
        if contains("Del", keysPressed(events, special)):
            current = current[:-1]
    return current

