from src.smart_agent import SmartAgent


class DeepAgent(SmartAgent):

    def pop_from_open_nodes(self, open_nodes):
        if open_nodes:
            return open_nodes.pop()
        return None
