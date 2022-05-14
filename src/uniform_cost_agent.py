from src.smart_agent import SmartAgent


class UniformCostAgent(SmartAgent):
    def pop_from_open_nodes(self, open_nodes):
        node_to_pop, idx_to_pop = open_nodes[0], 0
        for idx, node in enumerate(open_nodes):
            if len(node['environment'].winning_track) < len(node_to_pop['environment'].winning_track):
                node_to_pop = node
                idx_to_pop = idx
        return open_nodes.pop(idx_to_pop)
