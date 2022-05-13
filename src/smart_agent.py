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
        print(  self.counter)
        if self.graph.current_node is None:
            self.graph.visit_node(environment.hand)
        node_neighbors=[]

        for idx, card in enumerate(environment.hand):
            if self.disposable(environment.shown_card, card):
                node = [_card for _card in environment.hand if card != _card]
                throw_environment = environment._copy()
                throw_environment.act(card)
                node_neighbors.append(
                    {'thrown_card': card ,'node': node, 'environment': throw_environment})
        if not node_neighbors and environment.stack:
                buy_environment = environment._copy()
                buy_environment.act()
                buy_environment.victory_trail = [*environment.victory_trail, None]
                node_neighbors.append(
                    {'thrown_card': None, 'node': buy_environment.hand, 'environment': buy_environment})

        for neighbor in node_neighbors:
            self.graph.add_open_node(neighbor['thrown_card'], neighbor['node'], neighbor['environment'])

        if not node_neighbors:
            del environment
        if self.strategy == self.WIDE:
            target_node = self.graph.open_nodes.pop(0)
        else:
            target_node = self.graph.open_nodes.pop()

        self.graph.visit_node(target_node['node'])
        print(f"stack {len(target_node['environment'].stack)}")
        print(f"stack {len(target_node['environment'].hand)}")
        if not target_node['environment'].hand:
            return target_node['environment'].victory_trail

        if not self.graph.open_nodes and not target_node['environment'].stack:
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

