from collections import defaultdict


class Graph:
    # o set é usado para eliminar elementos repetidos
    visited_nodes = set()
    current_node = None
    neighbors=[]
    thrown_cards=[]
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def visit_node(self, node):
        self.visited_nodes.add(node)
        self.current_node=node


