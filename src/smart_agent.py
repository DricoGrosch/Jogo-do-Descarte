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
            self.graph.visual_graph.add_edge(self.graph.get_node_representation(environment.hand),self.graph.get_node_representation(neighbor['node']))
            self.graph.add_open_node(neighbor['thrown_card'], neighbor['node'], neighbor['environment'])
        if not node_neighbors:
            del environment
        if self.strategy == self.WIDE:
            target_node = self.graph.open_nodes.pop(0)
        else:
            target_node = self.graph.open_nodes.pop()

        self.graph.visit_node(target_node['node'])
        # print('-----------stack-----------------')
        # print(target_node['environment'].stack)
        # print()
        # print('-----------hand-----------------')
        # print(target_node['environment'].hand)
        # print('-----------shown card-----------------')
        # print(target_node['environment'].shown_card)
        # print('-----------victory trail-----------------')
        # print(target_node['environment'].victory_trail)

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



#
#
# {'thrown_card': None, 'node': ['8_Z', '21_Z', '3_Y', '19_W', '9_C', '23_Y', '26_Y', '20_Z', '16_W', '1_W', '14_W', '24_Z', '8_W', '2_Y', '4_X', '12_W', '13_C', '17_O', '4_E', '18_E', '24_X'], 'environment': <src.environment.Environment object at 0x00000153AB4E9960>}
# # -----------stack-----------------
# ['8_P', '16_Z', '25_Y', '18_Y', '9_Z', '13_X', '17_X', '17_C', '5_E', '19_P', '12_P', '11_C', '24_W', '18_O', '8_C', '6_C', '16_P', '21_C', '9_P', '24_E', '5_Z', '15_Z', '15_Y', '16_Y', '2_X', '9_E', '22_E', '15_C', '14_Y', '14_Y', '3_C', '10_P', '19_Y', '14_Z', '23_E', '26_E', '20_X', '11_E', '4_Y', '7_C', '14_P', '7_Z', '23_Z', '2_C', '15_X', '4_O', '20_Y', '18_W', '20_C', '20_E', '18_X', '8_X', '5_X', '12_Z', '2_P', '14_X', '16_O', '19_X', '23_W', '10_C', '25_Z', '16_E', '21_Y', '8_E', '14_W', '15_W', '4_Z', '13_Y', '7_O', '9_X', '11_O', '1_Z', '3_X', '8_Y', '11_Y', '3_O', '17_Z', '2_E', '3_Z', '11_W', '22_W', '5_W', '14_C', '9_Y', '12_C', '22_Y', '24_O', '22_Z', '20_O', '18_P', '14_E', '6_O', '24_C', '2_O', '21_X', '16_X', '19_O', '17_Y', '13_Z', '14_Z', '25_X', '10_O', '25_C', '14_X', '23_P', '22_C', '19_E', '25_E', '17_P', '6_X', '8_O', '26_C', '4_W', '16_C', '2_W', '4_C', '15_E', '24_P', '3_W', '18_C', '25_W', '14_O', '1_E', '13_P', '12_Y', '14_O', '1_X', '13_W', '26_X', '26_W', '26_Z', '2_Z', '6_Y', '24_Y', '17_W', '6_W', '21_P', '15_O', '10_Z', '12_E', '10_W', '19_C', '11_Z', '21_W', '18_Z', '10_Y', '11_X', '3_P', '9_O', '5_Y', '21_E', '14_E', '12_X', '1_Y', '10_X', '13_E', '20_W', '23_C', '7_X', '20_P', '17_E', '7_E', '11_P', '10_E', '21_O', '6_E', '23_X', '7_Y', '1_C', '1_P', '5_C', '5_P', '14_C', '22_X', '19_Z', '5_O', '3_E', '25_P', '13_O', '6_Z', '9_W', '14_P', '7_W', '23_O', '1_O']
#
# # -----------hand-----------------
# ['8_Z', '21_Z', '3_Y', '19_W', '9_C', '23_Y', '26_Y', '20_Z', '16_W', '1_W', '14_W', '24_Z', '8_W', '2_Y', '4_X', '12_W', '13_C', '17_O', '4_E', '18_E', '24_X']
# # -----------shown card-----------------
# 7_P
# # -----------victory trail-----------------
# [None, None, None, None, '12_O', None, '25_O', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '26_O', '26_P', '6_P', '22_P', '15_P', '4_P', '7_P', None, None, None, None, None]
# 2318
#
#
#
