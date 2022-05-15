from collections import defaultdict


class Graph:
    visited_nodes = []
    current_node = None
    open_nodes = []

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_nodes = []
        self.open_nodes = []
        self.current_node = None

    def is_new_node(self, node):
        for known_node in [*self.visited_nodes,*self.open_nodes]:
            if node['thrown_card'] == known_node['thrown_card'] and node['environment'].hand == known_node[
                'environment'].hand:
                return False
        return True

    def add_open_nodes(self, nodes):
        self.open_nodes.extend(nodes)

    def get_node_neighbors(self, node, branch_creation_callback):
        current_environment = node['environment']
        current_shown_card = node['environment'].shown_card
        current_hand = node['environment'].hand
        current_stack = node['environment'].stack
        node_neighbors = []
        for card in current_hand:
            if branch_creation_callback(current_shown_card, card):
                next_node_environment = current_environment._copy()
                next_node_environment.act(card)
                next_node_environment.winning_track.append(card)
                next_node = {'thrown_card': card, 'environment': next_node_environment}
                if self.is_new_node(next_node):
                    node_neighbors.append(next_node)
        if not node_neighbors and current_stack:
            next_node_environment = current_environment._copy()
            next_node_environment.act(None)
            next_node_environment.winning_track.append(None)
            next_node = {'thrown_card': None, 'environment': next_node_environment}
            if self.is_new_node(next_node):
                node_neighbors.append(next_node)
        return node_neighbors

    def visit_node(self, node):
        if node not in self.visited_nodes:
            self.visited_nodes.append(node)
            self.current_node = node
        else:
            print('node already visited')
