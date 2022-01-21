import pygame as pg
import time
import math
from Tools import rescale


#non-physical representation

BACKGROUND = rescale(pg.image.load('Resources/Background.png'), 3)

#playable models
MCAR = rescale(pg.image.load('Resources/MainCar.png'), 0.05)
COPS = rescale(pg.image.load('Resources/PoliceCar.png'), 0.01)

#important game objectsz
BORDER =rescale(pg.image.load('Resources/autotrack transparent.png'), 0.88)
FINISH = rescale(pg.image.load('Resources/Finish line.png'), 0.01)


WIN = pg.display.set_mode((795, 750))
pg.display.set_caption("SB")


FrameRate = 60

class BolidCars:
    def __init__(self, max_velocity, rotation_velocity):
        self.max_velocity = max_velocity
        self.rotation_velocity = rotation_velocity
        self.velocity = 0
        self.angle = 0

    def rotate ( )





def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)

play = True
clock = pg.time.Clock()
images = [(BACKGROUND,(0, 0)), (BORDER,(0, 0))]
while play:
    clock.tick(FrameRate)

    draw(WIN, images)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
            break
pg.quit()