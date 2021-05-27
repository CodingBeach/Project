# This will be whole game...

# //////////////////// Importing libraries
import os
import pygame
import threading,time
import numpy as np

# PyGame Initialization
pygame.init()
#
#
#
#  /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# ///////////////////// LAUNCHER \\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////
#
#
#
LAUNCHER_WINDOW = pygame.display.set_mode((1280, 720), pygame.NOFRAME)

# //////////////////// Launcher Background
launcher_background = pygame.image.load('assets/images/launcher/bg.png')

# //////////////////// Lau           Xpozycja  Ypozycja  Xwielkosc Ywielkosc
launcher_rect_login_input = pygame.Rect(502, 289, 280,36)
launcher_rect_password_input = pygame.Rect(502, 337, 280,36)
launcher_rect_login_button = pygame.Rect(748, 387, 32,36)
launcher_rect_register_button = pygame.Rect(504, 387, 238,36)
launcher_rect_exit_button = pygame.Rect(2, 678, 1276,40)
color = pygame.Color('lightskyblue3')


# //////////////////// Launcher IMAGES for: LOGIN INPUT, PASSWORD INPUT, LOGIN BUTTON, REGISTER BUTTON, EXIT BUTTON
launcher_login_input = pygame.image.load("assets/images/launcher/login_input.png")
launcher_password_input = pygame.image.load("assets/images/launcher/password_input.png")
launcher_login_button = pygame.image.load("assets/images/launcher/login_button.png")
launcher_register_button = pygame.image.load("assets/images/launcher/register_button.png")
launcher_exit_button = pygame.image.load("assets/images/launcher/exit_button.png")

# Sound
# mixer.music.load("assets/launcherd_screen.mp3")
# mixer.music.play(-1)

# Game Loop
launcherScreenEnabled = True
while launcherScreenEnabled:

    # Background Image
    LAUNCHER_WINDOW.blit(launcher_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Continue Game")

        if event.type == pygame.K_DOWN and event.key == pygame.K_ESCAPE:
            print("Continue Game")

    # draw here
    pygame.draw.rect(LAUNCHER_WINDOW,color,launcher_rect_login_input,1)
    pygame.draw.rect(LAUNCHER_WINDOW,color,launcher_rect_password_input,1)
    pygame.draw.rect(LAUNCHER_WINDOW,color,launcher_rect_login_button,1)
    pygame.draw.rect(LAUNCHER_WINDOW,color,launcher_rect_register_button,1)
    pygame.draw.rect(LAUNCHER_WINDOW,color,launcher_rect_exit_button,1)
    LAUNCHER_WINDOW.blit(launcher_login_input, (500, 287))
    LAUNCHER_WINDOW.blit(launcher_password_input, (500, 335))
    LAUNCHER_WINDOW.blit(launcher_login_button, (746, 385))
    LAUNCHER_WINDOW.blit(launcher_register_button, (502, 385))
    LAUNCHER_WINDOW.blit(launcher_exit_button, (0, 676))
    
    pygame.display.update()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#  /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
# //////////////////// PAUSE MENU \\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////
#
#
#
PAUSE_WINDOW = pygame.display.set_mode((1280, 720), pygame.NOFRAME)

# Background
pause_background = pygame.image.load('assets/images/backgrounds/background.jpg')

# Rectangles
pause_rect_continue = pygame.Rect(710, 390, 498,70)
pause_rect_options = pygame.Rect(710, 490, 498,70)
pause_rect_exit = pygame.Rect(710, 590, 498,70)
color = pygame.Color('lightskyblue3')


# Button1,2,3 images
pause_continue = pygame.image.load("assets/images/pause/continue.png")
pause_options = pygame.image.load("assets/images/pause/options.png")
pause_exit = pygame.image.load("assets/images/pause/exit.png")

# Sound
# mixer.music.load("assets/paused_screen.mp3")
# mixer.music.play(-1)

# Game Loop
pauseScreenEnabled = True
while pauseScreenEnabled:

    # Background Image
    PAUSE_WINDOW.blit(pause_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Continue Game")

        if event.type == pygame.K_DOWN and event.key == pygame.K_ESCAPE:
            print("Continue Game")

    # draw here
    pygame.draw.rect(PAUSE_WINDOW,color,pause_rect_continue,2)
    pygame.draw.rect(PAUSE_WINDOW,color,pause_rect_options,2)
    pygame.draw.rect(PAUSE_WINDOW,color,pause_rect_exit,2)
    PAUSE_WINDOW.blit(pause_continue, (710, 390))
    PAUSE_WINDOW.blit(pause_options, (710, 490))
    PAUSE_WINDOW.blit(pause_exit, (710, 590))
    
    pygame.display.update()