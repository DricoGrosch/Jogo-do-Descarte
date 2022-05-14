from src.a_star_agent import AStarAgent
from src.deep_agent import DeepAgent
from src.environment import Environment
# from src.smart_agent import SmartAgent
from src.wide_agent import WideAgent

import sys
sys.setrecursionlimit(10000)
env = Environment()
agent = AStarAgent(env)

while not env.finish():
    agent.step()



print(env.score())
print('adrian')
