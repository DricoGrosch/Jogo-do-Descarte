class Agent:
    def __init__(self, _env):
        self.env = _env

    def step(self):
        shown_card, hand = self.sense()
        try:
            self.act(shown_card, hand)
        except Exception as e:
            print(e)
        _victory_trail=[*self.env.victory_trail]
        for card in _victory_trail:
            self.env.act(card,False)
            self.env.victory_trail=list(filter(lambda _card: card!=_card,self.env.victory_trail))
        # print()

    def sense(self):
        shown_card, hand = self.env.sense()
        return shown_card, hand

    def act(self, shown_card, hand):
        raise NotImplemented

    def disposable(self, shown_card, card):
        shown_card_number, shown_card_suit = shown_card.split('_')
        c_number, c_suit = card.split('_')
        return (c_number == shown_card_number or c_suit == shown_card_suit)
