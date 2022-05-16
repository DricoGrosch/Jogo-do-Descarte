from src.environment import Environment


class SmartEnvironment(Environment):
    def finish(self):
        return len(self.hand) == 0


    def _copy(self):
        new_environment = SmartEnvironment()
        new_environment.shown_card = self.shown_card
        new_environment.stack = [*self.stack]
        new_environment.hand = [*self.hand]
        new_environment.winning_track = [*self.winning_track]
        return new_environment