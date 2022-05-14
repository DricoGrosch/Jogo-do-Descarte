from src.a_star_agent import AStarAgent
from src.deep_agent import DeepAgent
from src.environment import Environment
# from src.smart_agent import SmartAgent
from src.uniform_cost_agent import UniformCostAgent
from src.wide_agent import WideAgent

import sys
sys.setrecursionlimit(10000)
env = Environment(5)
agent = UniformCostAgent(env)

while not env.finish():
    agent.step()



print(env.score())
print('adrian')
