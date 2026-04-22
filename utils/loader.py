import pygame

def load_font(name, size):
    try:
        return pygame.font.SysFont(name,size)
    except:
        return pygame.font.Font(None, size)

def load_image(path):
    pass