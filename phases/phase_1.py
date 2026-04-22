import pygame
from models.player import Player

class Phase1:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.background = pygame.Surface((SCRESCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((50,50,50))

    def handle_event(self, event):

        pass

    def update(self, dt):

        keys = pygame.key.get_pressed()

        self.player.update(dt, keys)

        self.all_sprites.update(dt)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.all_sprites.draw(screen)
