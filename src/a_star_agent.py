from src.smart_agent import SmartAgent


class AStarAgent(SmartAgent):
    def pop_from_open_nodes(self, open_nodes):
        node_to_pop, idx_to_pop = open_nodes[0], 0
        for idx, node in enumerate(open_nodes):
            if len(node['environment'].hand) < len(node_to_pop['environment'].hand):
                node_to_pop = node
                idx_to_pop = idx
        return open_nodes.pop(idx_to_pop)
