from phases.level1 import Level1


class PhaseManager:
    def __init__(self, game):
        """Inicializa o gerenciador de fases."""
        self.game = game

    def get_initial_phase(self):
        """Retorna a fase inicial do jogo."""
        return Level1(self.game)    