from src.environment import Environment
from src.smart_agent import SmartAgent

env = Environment(5)
agent = SmartAgent(strategy=SmartAgent.WIDE,_env=env)
import sys
sys.setrecursionlimit(3000)
while not env.finish():
    agent.step()
print(env.score())
# pra cada nó (cada jogada) verificar as cartas que eu posso descartar e pra cada uma criar uma ramificação
