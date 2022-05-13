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
        self.visual_graph=nx.Graph()

    def get_node_representation(self,node):
        return '|'.join(node)

    def visit_node(self, node):
        if node not in self.visited_nodes:
            self.visited_nodes.append(node)
        self.current_node = node

    def show_png(self,counter):
        nx.draw(self.visual_graph, with_labels=True)
        plt.savefig(f'graph_{counter}.png')
        # plt.show()
    def add_open_node(self, thrown_card, node, environment):
        self.open_nodes.append({
            'thrown_card': thrown_card,
            'node': node,
            'environment': deepcopy(environment)})
