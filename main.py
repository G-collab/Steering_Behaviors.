import pygame as pg
import time
import math
from Tools import rescale,bl_center_rotate


#non-physical representation

BACKGROUND = rescale(pg.image.load('Resources/Background.png'), 3)

#playable models
MCAR = rescale(pg.image.load('Resources/MainCar.png'), 0.07)
COPS = rescale(pg.image.load('Resources/PoliceCar.png'), 0.01)

#important game objectsz

BORDER =rescale(pg.image.load('Resources/autotrack transparent.png'), 0.88)
FINISH = rescale(pg.image.load('Resources/Finish line.png'), 0.01)

#pygame window
WIN = pg.display.set_mode((795, 750))
pg.display.set_caption("SB")

FrameRate = 120


class BolidCars:
    def __init__(self, max_velocity, rotation_velocity):
        self.img = self.IMG
        self.max_velocity = max_velocity
        self.velocity = 0
        self.rotation_velocity = rotation_velocity
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_velocity
        elif right:
            self.angle -= self.rotation_velocity

    def draw(self, win):
        bl_center_rotate(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration, self.max_velocity)
        self.move()

    def move_backwards(self):
        self.velocity = min(self.velocity - self.acceleration, self.max_velocity / 3)
        self.move()

    def move(self):
        rad = math.radians(self.angle)
        vertical = math.cos(rad) * self.velocity
        horizon = math.sin(rad) * self.velocity
        self.y -= vertical
        self.x -= horizon

    def speed_down(self):
        self.velocity = max(self.max_velocity - self.acceleration / 2, 0)
        self.move()


class PlayerCar(BolidCars):
    IMG = MCAR
    START_POS = (145, 200)


def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pg.display.update()


run = True
clock = pg.time.Clock()
images = [(BACKGROUND, (0, 0)), (BORDER, (0, 0))]
player_car = PlayerCar(4, 4)

while run:
    clock.tick(FrameRate)

    draw(WIN, images, player_car)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break

    controls = pg.key.get_pressed()


    if controls[pg.K_a]:
        player_car.rotate(left=True)
    if controls[pg.K_d]:
        player_car.rotate(right=True)

    if controls[pg.K_w]:

        player_car.move_forward()

    if controls[pg.K_s]:

        player_car.move_backwards()



pg.quit()