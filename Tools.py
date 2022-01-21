import pygame

def rescale(img, x):
    size = round(img.get_height()* x), round(img.get_width() * x)
    return pygame.transform.scale(img, size)