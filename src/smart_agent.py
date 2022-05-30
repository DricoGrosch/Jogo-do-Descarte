import datetime

from src.agent import Agent
from src.graph import Graph


class SmartAgent(Agent):
    graph = None
    counter = 0

    def pop_from_open_nodes(self, open_nodes):
        raise NotImplemented

    def step(self):
        if not self.graph:
            self.graph = Graph()
            self.graph.visit_node({'thrown_card': None, 'environment': self.env})
            winning_track, lost = self.build_winning_tracks()
            if lost:
                return
            self.env.winning_track = winning_track
        super(SmartAgent, self).step()

    def act(self, shown_card, hand):
        try:
            card = self.env.winning_track.pop(0)
            return card
        except Exception as e:
            print(e)

    def get_node_neighbors(self, node):
        return

    def build_winning_tracks(self):
        meta_node_found = False
        winning_track = []
        start = datetime.datetime.now()
        while (not meta_node_found and not self.lost):
            current = datetime.datetime.now()
            self.lost = ((current - start).total_seconds() / 60) > 1
            self.counter += 1
            # print(self.counter)
            current_environment = self.graph.current_node['environment']
            if current_environment.finish():
                winning_track = current_environment.winning_track
                meta_node_found = True
                continue
            current_node_neighbors = self.graph.get_node_neighbors(self.graph.current_node, self.disposable)
            self.graph.add_open_nodes(current_node_neighbors)
            next_node_to_visit = self.pop_from_open_nodes(self.graph.open_nodes)
            if next_node_to_visit:
                self.graph.visit_node(next_node_to_visit)
        print(f'winning_track-->{winning_track}')
        return winning_track, self.lost
