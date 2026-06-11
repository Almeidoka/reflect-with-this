from phases.phase_1 import Phase1


class PhaseManager:
    def __init__(self, game):
        self.game = game

    def get_initial_phase(self):
        return Phase1(self.game)
