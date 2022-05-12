from collections import defaultdict
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    # o set é usado para eliminar elementos repetidos
    visited_nodes = []
    current_node = None
    open_nodes = []

    def __init__(self):
        self.graph = defaultdict(list)

    def visit_node(self, node):
        if node not in self.visited_nodes:
            self.visited_nodes.append(node)
        self.current_node = node

    def get_node_representation(self, node):
        return '|'.join(node['node'])

    def add_open_node(self, thrown_card, node, environment):
        self.open_nodes.append({
            'thrown_card': thrown_card,
            'node': node,
            'environment': deepcopy(environment)})
        # print(f'{thrown_card}-->|{node}|')