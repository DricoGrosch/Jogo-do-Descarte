from collections import defaultdict


class Graph:
    # o set é usado para eliminar elementos repetidos
    visited_nodes = set()

    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def visit_node(self, node):
        self.visited_nodes.add(node)

