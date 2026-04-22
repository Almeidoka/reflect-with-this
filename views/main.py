import pygame
from pygame import Rect

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False

    def draw(self, surface, font):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2, border_radius=10)
        
        text_surf = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        return self.is_hovered

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.action:
                self.action()

class MainView:
    def __init__(self, game):
        self.game = game
        self.buttons = []
        self._setup_ui()

    def _setup_ui(self):
        # Botão Play
        play_button = Button(
            x=300, y=200, width=200, height=50,
            text="Play", 
            color=(50, 50, 200),
            hover_color=(70, 70, 230),
            action=self.game.start_game
        )
        
        # Botão Options
        options_button = Button(
            x=300, y=300, width=200, height=50,
            text="Options", 
            color=(200, 50, 50),
            hover_color=(230, 70, 70),
            action=self.game.show_options
        )
        
        self.buttons = [play_button, options_button]

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            for button in self.buttons:
                button.check_hover(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                button.handle_event(event)

    def update(self):
        pass  # Pode adicionar animações ou lógica de atualização aqui

    def render(self, surface):
        # Renderiza título
        title_font = self.game.assets['fonts']['title']
        button_font = self.game.assets['fonts']['button']
        
        title_surf = title_font.render("MEU JOGO", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(400, 100))
        surface.blit(title_surf, title_rect)
        
        # Renderiza botões
        for button in self.buttons:
            button.draw(surface, button_font)