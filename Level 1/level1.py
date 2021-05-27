import pygame
import sys
pygame.init()


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

FPS = 60
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('assets/fonts/navine-demo.semicondensed', 20)
background = pygame.image.load('assets/images/backgrounds/background.jpg')
icon = pygame.image.load("assets/images/icons/icon.png")

# /////////////////////////////////////////////////////// CREATING THE MAIN GAME WINDOW
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# /////////////////////////////////////////////////////// SETTING TITLE OF THE GAME TO THE CAPTION OF THE WINDOW
pygame.display.set_caption('The Game - Level 1')

# /////////////////////////////////////////////////////// SETTING THE ICON TO THE ASSIGNED ICON IMAGE (variable)
pygame.display.set_icon(icon)





# /////////////////////////////////////////////////////// KLASA DOLNEJ PLATFORMY
class Dolnaplatforma:
    def __init__(self):
        self.dolnaplatforma_img = pygame.image.load('assets/images/game/dolnaplatforma.png')
        self.dolnaplatforma_img_rect = self.dolnaplatforma_img.get_rect()
        self.dolnaplatforma_img_rect.left = 0
        self.dolnaplatforma_img_rect.top = 1010
    def update(self):
        WIN.blit(self.dolnaplatforma_img, self.dolnaplatforma_img_rect)
#
#
#
#
#
# /////////////////////////////////////////////////////// SETTING TITLE OF THE GAME TO THE CAPTION OF THE WINDOW
def game_over_screen():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('Level 1/gameover.wav')
    music.play()
    game_over_screen_img = pygame.image.load('Level 1/end.png')
    game_over_screen_img_rect = game_over_screen_img.get_rect()
    game_over_screen_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()

def start_game():
    start_img = pygame.image.load('Level 1/start.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    WIN.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()

def game_loop():
    while True:
        dolnaplatforma = Dolnaplatforma()
        pygame.mixer.music.load('Level 1/mario_theme.wav')
        pygame.mixer.music.play(-1, 0.0)
        while True:

# /////////////////////////////////////////////////////// BLITTING THE BACKGROUND
            WIN.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

# /////////////////////////////////////////////////////// WHEN ESCAPE pressed GAME CLOSES 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

            dolnaplatforma.update()
            pygame.display.update()
            CLOCK.tick(FPS)

start_game()


