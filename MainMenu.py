# Importing libraries
import os
import pygame
import cv2
from pygame.constants import GL_CONTEXT_ROBUST_ACCESS_FLAG
import pyglet
import moviepy
from moviepy.editor import *
from moviepy.decorators import convert_masks_to_RGB, requires_duration
from moviepy.video.io.preview import imdisplay,show
import threading,time
import numpy as np
from moviepy.video.fx import *
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

## Video Represent
def exitOp(isAudio,videoFlag,audiothread): ## just exiting the threads needed for the video displaying. CALL THIS WHEN EXITING THE CLIP
    if isAudio and videoFlag != None and audiothread != None:
        videoFlag.clear()
        audiothread.join()

class Button:
    def __init__(self,height,width,x,y,img):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.img = img
        self.wasClicked = False

@requires_duration
@convert_masks_to_RGB
def preview(clip, screen, buttons, fps=60, audio=True, audio_fps=22050, audio_buffersize=3000, audio_nbytes=2, fullscreen=True):

    if fullscreen:
        flags = pygame.FULLSCREEN
    else:
        flags = 0
    
    audio = audio and (clip.audio is not None)

    audiothread = None
    videoFlag = None
    if audio:
        videoFlag = threading.Event()
        audioFlag = threading.Event()
        audiothread = threading.Thread(target=clip.audio.preview,
                                       args=(audio_fps,
                                             audio_buffersize,
                                             audio_nbytes,
                                             audioFlag, videoFlag))
        audiothread.start()
    
    img = clip.get_frame(0)
    imdisplay(img, screen)
    if audio:  # synchronize with audio
        videoFlag.set()  # say to the audio: video is ready
        audioFlag.wait()  # wait for the audio to be ready
    
    result = []
    
    t0 = time.time()

    for t in np.arange(1.0 / fps, clip.duration-.001, 1.0 / fps):
        img = clip.get_frame(t)
        videoFrame = pygame.surfarray.make_surface(img.swapaxes(0, 1))
        screen.blit(videoFrame, (0,0))
	
        ## STANDARD EVENT COLLECTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitOp(audio, videoFlag, audiothread)
                return True

# If you press ESCAPE key, the launcher quits
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        ## DRAW STUFF HERE


        ## ----------------

        t1 = time.time()
        time.sleep(max(0, t - (t1-t0)))

        pygame.display.update()


    return False

## START OF YOUR CODE

print(os.getcwd())

# Initialization the PyGame
pygame.init()

# Create the screen
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#WIN_MINIMIZED = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
# Menu Background
# background = pygame.image.load('Assets/background.png') /////////////////////////////////////////////////////////////////////////////////////

# Game TITLE and ICON
pygame.display.set_caption("Game Launcher") # title of the game
icon = pygame.image.load('assets/icon.png') # define the icon variable ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.display.set_icon(icon) # set the window icon to the icon variable //////////////////////////////////////////////////////////////////////////////////////////////////////

# FPS Lock
FPS = 60

#Clip 
clip = VideoFileClip("assets/particles.mp4")


# preview(clip,WIN,[button1],fullscreen = True) # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
while True:
    if preview(clip,WIN,[]):
        break