from src.dummy_agent import DummyAgent
from src.environment import Environment

env = Environment()
agent = DummyAgent(env)

while not env.finish():
    agent.step()
print(env.score())
