import pygame
import time
import math


#non-physical representation
TRACK = pygame.image.load('Resources/Track.png')
BACKGROUND = pygame.image.load('Resources/Background.png')

#playable models
MCAR = pygame.image.load('Resources/MainCar.png')
COPS = pygame.image.load('Resources/PoliceCar.png')

#important game objectsz
BORDER = pygame.image.load('Resources/autotrack transparent.png')
FINISH = pygame.image.load('Resources/Finish line.png')

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SB")


play = True
while play:

    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(TRACK, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            play = False
            break
pygame.quit()