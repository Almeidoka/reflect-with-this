import pygame
from models.player import Player
from config.settings import *

class Phase1:
    def __init__(self, game):
        self.game = game
        self.all_sprites = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((50, 50, 50)) #Fundo cinza


    def handle_event(self, event) :
        
        pass #pode adicionar eventos específicos aqui

    def update(self, dt) :
        """Atualiza todos os objetos da fase."""
        keys = pygame.key.get_pressed()

        self.player.update(dt, keys)


        self.all_sprites.update(dt)

    def draw(self, screen):

        screen.blit(self.background, (0,0))
        self.all_sprites.draw(screen)

         