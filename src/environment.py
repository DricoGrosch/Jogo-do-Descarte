import random

VERBOSE = False


class Environment:
    shown_card = None
    stack = None
    hand = None
    winning_track = []

    def __init__(self, seed=None):
        self.setup(seed)

    def setup(self, seed=None):
        if seed:
            random.seed(seed)
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['P', 'C', 'E', 'O']
        all_cards = []
        for number in numbers:
            for suit in suits:
                all_cards.append(f'{number}_{suit}')

        random.shuffle(all_cards)
        self.hand = all_cards[:5]
        self.shown_card = all_cards[5]
        self.stack = all_cards[6:]

    def finish(self):
        return len(self.hand) == 0 or len(self.stack) == 0

    def score(self):
        return len(self.stack) - len(self.hand)

    def sense(self):
        return self.shown_card, self.hand

    def buy_card(self):
        self.hand.append(self.stack.pop())

    def dispose_card(self, card):
        self.hand.remove(card)
        self.shown_card = card

    def _copy(self):
        new_environment = Environment()
        new_environment.shown_card = self.shown_card
        new_environment.stack = [*self.stack]
        new_environment.hand = [*self.hand]
        new_environment.winning_track = [*self.winning_track]
        return new_environment

    def act(self, card):
        self.dispose_card(card) if card else self.buy_card()
