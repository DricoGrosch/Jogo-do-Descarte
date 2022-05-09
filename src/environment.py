import random

VERBOSE = False


class Environment:
    shown_card = None
    stack = None
    hand = None

    def __init__(self, seed=None):
        self.setup(seed)

    def setup(self, seed=None):
        if seed is not None: random.seed(seed)

        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['P', 'C', 'E', 'O']
        all_cards = []
        for number in numbers:
            for suit in suits:
                all_cards.append(number + '_' + suit)

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

    def act(self, action):
        if VERBOSE:
            print('Shown card is %s' % self.shown_card)
            print('Hand is', self.hand)
        if action is not None:
            if VERBOSE: print('Disposing card %s\n---' % action)
            self.hand.remove(action)
            self.shown_card = action
        else:
            if VERBOSE: print('Getting card %s from stack\n---' % self.stack[-1])
            self.hand.append(self.stack.pop())