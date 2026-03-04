import pygame
from phases.phase_manager import PhaseManager


class Game:
    def __init__(self, screen):
        """Inicializa o jogo principal."""
        self.screen = screen
        self.phase_manager = PhaseManager(self)
        self.current_phase = self.phase_manager.get_initial_phase()

    def handle_event(self, event):
        """Delega o tratamento de eventos para a fase atual."""
        self.current_phase.handle_event(event)

    def update(self, dt):
        """Atualiza a fase atual."""
        self.current_phase.update(dt)

    def draw(self, screen):
        """Desenha a fase atual."""
        self.current_phase.draw(screen)