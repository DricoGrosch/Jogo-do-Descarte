class Agent:
    lost = False

    def __init__(self, _env):
        self.env = _env

    def step(self):
        shown_card, hand = self.sense()
        card = self.act(shown_card, hand)
        self.env.act(card)

    def sense(self):
        shown_card, hand = self.env.sense()
        return shown_card, hand

    def act(self, shown_card, hand):
        raise NotImplemented

    def disposable(self, shown_card, card):
        shown_card_number, shown_card_suit = shown_card.split('_')
        c_number, c_suit = card.split('_')
        return (c_number == shown_card_number or c_suit == shown_card_suit)
