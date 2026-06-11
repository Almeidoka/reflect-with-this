import pygame
from config.settings import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Inicializa o personagem do jogador."""
        super().__init__()

        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()

        self.rect.center = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2
        )

        self.speed = PLAYER_SPEED
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self, dt, keys):
        """Atualiza a posição do jogador."""
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity.y = -self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity.y = self.speed

        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize() * self.speed

        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

        self.rect.x = max(
            0,
            min(self.rect.x, SCREEN_WIDTH - self.rect.width)
        )

        self.rect.y = max(
            0,
            min(self.rect.y, SCREEN_HEIGHT - self.rect.height)
        )
