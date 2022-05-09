import statistics

from src.dummy_agent import DummyAgent
from src.environment import Environment

results = []
for _ in range(1000):
    env = Environment()
    agent = DummyAgent(env)

    while not env.finish():
        agent.step()
    results.append(env.score())

print('RESULTS')
print(f'Number of samples: {len(results)}')
print(f'Wins: {sum([1 for x in results if x >= 0])}')
print(f'Losses: {sum([1 for x in results if x < 0])}')
print(f'Mean score: {round(statistics.mean(results),2)}')
print(f'Standard deviation (score): {round(statistics.stdev(results),2)}')
print(f'Median score: {round(statistics.median(results),2)}')
