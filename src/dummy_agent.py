from src.agent import Agent


class DummyAgent(Agent):

    def act(self, shown_card, hand):
        for card in hand:
            if self.disposable(shown_card, card):
                return card
        return None