from src.smart_agent import SmartAgent


class WideAgent(SmartAgent):

    def pop_from_open_nodes(self, open_nodes):
        if open_nodes:
            return open_nodes.pop(0)
        return None
