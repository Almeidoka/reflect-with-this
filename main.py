import pygame
from core.game import Game


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    game = Game(screen)

    game.run()
