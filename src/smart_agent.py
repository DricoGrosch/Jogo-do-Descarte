from src.agent import Agent
from src.graph import Graph


class SmartAgent(Agent):
    graph = None

    def pop_from_open_nodes(self, open_nodes):
        raise NotImplemented

    def step(self):
        if not self.graph:
            self.graph = Graph()
            self.graph.visit_node({'thrown_card': None, 'environment': self.env})
            winning_track = self.build_winning_tracks()
            self.env.winning_track = winning_track
        super(SmartAgent, self).step()

    def act(self, shown_card, hand):
        card = self.env.winning_track.pop(0)
        return card

    def get_node_neighbors(self, node):
        return

    def build_winning_tracks(self):
        current_environment = self.graph.current_node['environment']
        if current_environment.finish():
            return current_environment.winning_track
        current_node_neighbors = self.graph.get_node_neighbors(self.graph.current_node, self.disposable)
        self.graph.add_open_nodes(current_node_neighbors)
        next_node_to_visit = self.pop_from_open_nodes(self.graph.open_nodes)
        if next_node_to_visit:
            self.graph.visit_node(next_node_to_visit)
            return self.build_winning_tracks()
        else:
            print()
