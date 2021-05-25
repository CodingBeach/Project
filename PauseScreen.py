# Importing libraries
import os
import pygame
import cv2
from pygame.constants import GL_CONTEXT_ROBUST_ACCESS_FLAG
import pyglet
import threading,time
import numpy as np
import math
import random
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the pauseScreen
pauseScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.NOFRAME)

# Background
background = pygame.image.load('assets/background.jpg')

# Rectangles
rect_button1 = pygame.Rect(710, 390, 498,48)
rect_button2 = pygame.Rect(710, 490, 498,48)
rect_button3 = pygame.Rect(710, 590, 498,48)
color = pygame.Color('lightskyblue3')


# Button1,2,3 images
button1 = pygame.image.load("assets/continue_button.png")
button2 = pygame.image.load("assets/options_button.png")
button3 = pygame.image.load("assets/exit_to_menu_button.png")

# Sound
# mixer.music.load("assets/paused_screen.mp3")
# mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Pause Screen")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# Game Loop
pauseScreenEnabled = True
while pauseScreenEnabled:

    # Background Image
    pauseScreen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pauseScreenEnabled = False

    # draw here
    pygame.draw.rect(pauseScreen,color,rect_button1,2)
    pygame.draw.rect(pauseScreen,color,rect_button2,2)
    pygame.draw.rect(pauseScreen,color,rect_button3,2)
    pauseScreen.blit(button1, (710, 390))
    pauseScreen.blit(button2, (710, 490))
    pauseScreen.blit(button3, (710, 590))
    
    pygame.display.update()