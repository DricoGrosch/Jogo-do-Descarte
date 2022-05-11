from src.dummy_agent import DummyAgent
from src.environment import Environment

env = Environment()
agent = DummyAgent(env)

while not env.finish():
    agent.step()
print(env.score())
# pra cada nó (cada jogada) verificar as cartas que eu posso descartar e pra cada uma criar uma ramificação
