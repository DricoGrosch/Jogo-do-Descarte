import random

VERBOSE = False


class Environment:
    shown_card = None
    stack = None
    hand = None
    victory_trail = []

    def __init__(self, seed=None):
        self.setup(seed)

    def setup(self, seed=None):
        if seed:
            random.seed(seed)
        # numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13','14','15']
        # suits = ['P', 'C', 'E', 'O']
        # numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # suits = ['P', 'C', 'E', 'O']
        # numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # suits = ['P', 'C', 'E', 'O']

        # numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '14', '15', '16', '17',
        #            '18', '19', '20', '21', '22', '23', '24', '25', '26']
        # suits = ['P', 'C', 'E', 'O', 'X', 'Y', 'Z', 'W']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['P', 'C', 'E', 'O']
        # numbers = ['1', '2', '3', '4', '5', '6', '7','8','9']
        # suits = ['P', ]
        all_cards = []
        for number in numbers:
            for suit in suits:
                all_cards.append(f'{number}_{suit}')

        random.shuffle(all_cards)
        self.hand = all_cards[:5]
        self.shown_card = all_cards[5]
        self.stack = all_cards[6:]

    def finish(self):
        if not self.hand:
            return True
        if not self.stack and self.victory_trail:
            return False
        if not self.stack and not self.victory_trail:
            return True
        return False

    def score(self):
        return len(self.stack) - len(self.hand)

    def _copy(self):
        new_environment = Environment()
        new_environment.shown_card = self.shown_card
        new_environment.stack = [*self.stack]
        new_environment.hand = [*self.hand]
        new_environment.victory_trail = [*self.victory_trail]
        return new_environment

    def sense(self):
        return self.shown_card, self.hand

    def buy_card(self):
        self.hand.append(self.stack.pop())

    def dispose_card(self, card):
        try:
            self.hand.remove(card)
            self.shown_card = card
        except Exception as e:
            print(e)

    def act(self, card=None, add_victory_trail=True):
        self.dispose_card(card) if card else self.buy_card()
        if add_victory_trail:
            self.victory_trail.append(card)

