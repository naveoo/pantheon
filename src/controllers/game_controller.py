from src.models.religion import Religion

class GameController:
    def __init__(self):
        self.religions = []
        self.initialize_game()

    def initialize_game(self):
        self.religions.append(Religion("Sun Lovers", "athéisme", "bagdad"))

    def start(self):
        running = True
        while running:
            pass
