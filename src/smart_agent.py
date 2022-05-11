from copy import copy

from src.agent import Agent
from src.graph import Graph


class SmartAgent(Agent):
    DEEP = 1
    WIDE = 2
    strategy = None
    graph = None

    def __init__(self, strategy=DEEP, *args, **kwargs):
        self.strategy = strategy
        self.graph = Graph()
        super(SmartAgent, self).__init__(*args, **kwargs)

    def handle_strategy(self, environment):
        if self.graph.current_node is None:
            self.graph.visit_node(environment.hand)
        for idx, card in enumerate(environment.hand):
            if self.disposable(environment.shown_card, card):
                node = [card for idx, card in enumerate(environment.hand)]
                self.graph.neighbors.append({'thrown_card': card, 'node': node})

        # tenho a nova mao e o novo monte com o buy_card
        environment.buy_card()
        # environment.hand passa a ser com a carta comprada
        self.graph.neighbors.append({'thrown_card':None,'node':environment.hand})

        # a partir daqui tenho todos os vizinhos com as cardas jogaveis e também o vizinho com um acarta comprada
        if self.strategy == self.WIDE:
            target_node = self.graph.neighbors.pop()
            self.graph.thrown_cards.append(target_node['thrown_card'])
            self.graph.visit_node(target_node['node'])
        else:
            target_node = self.graph.neighbors.pop(0)
            self.graph.thrown_cards.append(target_node['thrown_card'])
            self.graph.visit_node(target_node['node'])
        if environment.finish():
            return self.graph.visited_nodes[0]
        self.handle_strategy(environment)

    def act(self, shown_card, hand):
        if not self.graph.thrown_cards:
            card_to_throw = self.handle_strategy(copy(self.env))
        else:
            card_to_throw=self.graph.thrown_cards.pop(0)
        return card_to_throw
