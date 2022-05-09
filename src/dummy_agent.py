class DummyAgent:
    def __init__(self, _env):
        self.env = _env

    def step(self):
        shown_card, hand = self.sense()
        action = self.act(shown_card, hand)
        self.env.act(action)

    def sense(self):
        shown_card, hand = self.env.sense()
        return shown_card, hand

    def act(self, shown_card, hand):
        for card in hand:
            if self.disposable(shown_card, card):
                return card
        return None

    def disposable(self, shown_card, card):
        number = shown_card.split('_')[0]
        suit = shown_card.split('_')[1]
        c_number = card.split('_')[0]
        c_suit = card.split('_')[1]
        return (c_number == number or c_suit == suit)