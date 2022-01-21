import pygame as pg

#rescaling images from sources


def rescale(img, x):
    size = round(img.get_height()* x), round(img.get_width() * x)
    return pg.transform.scale(img, size)


def bl_center_rotate(win, image, top_left, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)
