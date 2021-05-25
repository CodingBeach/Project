import pygame
import sys
pygame.init()


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

FPS = 60
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)
background = pygame.image.load('assets/background.jpg')

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Mario')

class Mario:
    velocity = 2

    def __init__(self):
        self.mario_img = pygame.image.load('SimpleMarioGame/maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = WINDOW_HEIGHT/2 - 100
        self.down = True
        self.up = False
        self.right = False
        self.left = False

    def update(self):
        WIN.blit(self.mario_img, self.mario_img_rect)
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10
        if self.right:
            self.mario_img_rect.top -= 10
        if self.left:
            self.mario_img_rect.bottom += 10

class Dolnaplatforma:
    def __init__(self):
        self.dolnaplatforma_img = pygame.image.load('assets/dolnaplatforma.png')
        self.dolnaplatforma_img_rect = self.dolnaplatforma_img.get_rect()
        self.dolnaplatforma_img_rect.left = 0
        self.dolnaplatforma_img_rect.top = 1010

    def update(self):
        WIN.blit(self.dolnaplatforma_img, self.dolnaplatforma_img_rect)


def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('SimpleMarioGame/mario_dies.wav')
    music.play()
    game_over_img = pygame.image.load('SimpleMarioGame/end.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
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
    start_img = pygame.image.load('SimpleMarioGame/start.png')
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
        mario = Mario()
        dolnaplatforma = Dolnaplatforma()
        pygame.mixer.music.load('SimpleMarioGame/mario_theme.wav')
        pygame.mixer.music.play(-1, 0.0)
        while True:
            WIN.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        mario.left = True
                    elif event.key == pygame.K_DOWN:
                        mario.left = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        mario.right = True
                    elif event.key == pygame.K_DOWN:
                        mario.right = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False

            mario.update()
            dolnaplatforma.update()
            pygame.display.update()
            CLOCK.tick(FPS)

start_game()


