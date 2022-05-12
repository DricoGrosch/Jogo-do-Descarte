from copy import deepcopy

from src.agent import Agent
from src.graph import Graph


class SmartAgent(Agent):
    DEEP = 1
    WIDE = 2

    A_STAR = 4
    strategy = None
    graph = None

    def __init__(self, strategy=DEEP, *args, **kwargs):
        self.strategy = strategy
        self.graph = Graph()
        super(SmartAgent, self).__init__(*args, **kwargs)

    def handle_strategy(self, environment):
        print()
        print('---------------------------------')
        print()
        if self.graph.current_node is None:
            self.graph.visit_node(environment.hand)
        # print(f'THROWN CARDS-->{environment.thrown_cards}')
        # print(f'CURRENT NODE --> {self.graph.current_node}')
        # print(f'SHOWN CARD --> {environment.shown_card}')

        # print(f'CURRENT HAND--> {environment.hand}')
        print(f'hand-->{len(environment.hand)}')
        print(f'stack-->{len(environment.stack)}')
        for idx, card in enumerate(environment.hand):
            if self.disposable(environment.shown_card, card):
                node = [_card for _card in environment.hand if card != _card]
                self.graph.add_open_node(card, node, environment)

        _environment = deepcopy(environment)
        _environment.act()
        # environment.hand passa a ser com a carta comprada
        self.graph.add_open_node(None, _environment.hand, _environment)

        # a partir daqui tenho todos os vizinhos com as cardas jogaveis e também o vizinho com um acarta comprada
        if self.strategy == self.WIDE:
            target_node = self.graph.open_nodes.pop(0)
        else:
            target_node = self.graph.open_nodes.pop()


        # print(f"TARGET NODE --> {target_node['node']} THROWING {target_node['thrown_card']}")
        self.graph.visit_node(target_node['node'])
        try:
            target_node['environment'].act(target_node['thrown_card'])
        except Exception as e:
            print(e)

        if target_node['environment'].finish():
            return self.graph.visited_nodes[0]
        return self.handle_strategy(target_node['environment'])

    def act(self, shown_card, hand):
        if not self.env.thrown_cards:
            card_to_throw = self.handle_strategy(deepcopy(self.env))
        else:
            card_to_throw = self.env.thrown_cards.pop(0)
        return card_to_throw
# thrown_cards tem que ficar no ambiente