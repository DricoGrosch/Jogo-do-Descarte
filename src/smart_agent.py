from copy import deepcopy, copy

from src.agent import Agent
from src.environment import Environment
from src.graph import Graph


class SmartAgent(Agent):
    DEEP = 1
    WIDE = 2

    A_STAR = 4
    strategy = None
    graph = None
    counter=0
    def __init__(self, strategy=DEEP, *args, **kwargs):
        self.strategy = strategy
        self.graph = Graph()
        super(SmartAgent, self).__init__(*args, **kwargs)

    def handle_strategy(self, environment):
        self.counter += 1
        # if(self.counter==1000):
        #     print()
        print(self.counter)
        print('---------------------------------')
        print()
        if self.graph.current_node is None:
            self.graph.visit_node(environment.hand)

        print(f'hand-->{len(environment.hand)}')
        print(f'stack-->{len(environment.stack)}')

        if environment.stack:
            buy_environment = environment._copy()
            buy_environment.act()
            buy_environment.victory_trail = [*environment.victory_trail, None]
            self.graph.add_open_node(None, buy_environment.hand, buy_environment)

        for idx, card in enumerate(environment.hand):
            if self.disposable(environment.shown_card, card):
                node = [_card for _card in environment.hand if card != _card]
                throw_environment = environment._copy()
                throw_environment.act(card)
                self.graph.add_open_node(card, node, throw_environment)


        if self.strategy == self.WIDE:
            target_node = self.graph.open_nodes.pop(0)
        else:
            target_node = self.graph.open_nodes.pop()

        self.graph.visit_node(target_node['node'])

        if not target_node['environment'].hand:
            return target_node['environment'].victory_trail

        if not self.graph.open_nodes:
            return None

        return self.handle_strategy(target_node['environment'])

    def act(self, shown_card, hand):
        if not self.env.victory_trail:
            victory_trail = self.handle_strategy(self.env._copy())
            self.env.victory_trail = victory_trail
            card_to_throw = self.env.victory_trail.pop(0)
        else:
            card_to_throw = self.env.victory_trail.pop(0)
        return card_to_throw

