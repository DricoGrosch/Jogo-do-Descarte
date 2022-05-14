import statistics

from src.deep_agent import DeepAgent
from src.dummy_agent import DummyAgent
from src.environment import Environment
import sys

from src.wide_agent import WideAgent

sys.setrecursionlimit(10000)

dummy_results = []
wide_results = []
deep_results = []

#
# for _ in range(1000):
#     env = Environment()
#     agent = DummyAgent(env)
#
#     while not env.finish():
#         agent.step()
#     dummy_results.append(env.score())
#
# print('DUMMY RESULTS')
# print(f'Number of samples: {len(dummy_results)}')
# print(f'Wins: {sum([1 for x in dummy_results if x >= 0])}')
# print(f'Losses: {sum([1 for x in dummy_results if x < 0])}')
# print(f'Mean score: {round(statistics.mean(dummy_results),2)}')
# print(f'Standard deviation (score): {round(statistics.stdev(dummy_results),2)}')
# print(f'Median score: {round(statistics.median(dummy_results),2)}')
#
# for _ in range(1000):
#     env = Environment()
#     agent = DeepAgent(env)
#
#     while not env.finish():
#         agent.step()
#     deep_results.append(env.score())
# print()
# print('--------------------')
# print()
#
# print('DEEP RESULTS')
# print(f'Number of samples: {len(deep_results)}')
# print(f'Wins: {sum([1 for x in deep_results if x >= 0])}')
# print(f'Losses: {sum([1 for x in deep_results if x < 0])}')
# print(f'Mean score: {round(statistics.mean(deep_results),2)}')
# print(f'Standard deviation (score): {round(statistics.stdev(deep_results),2)}')
# print(f'Median score: {round(statistics.median(deep_results),2)}')
#
for _ in range(5):
    env = Environment(5)
    agent = WideAgent(env)
    while not env.finish():
        agent.step()
    wide_results.append(env.score())


print('WIDE RESULTS')
print(f'Number of samples: {len(wide_results)}')
print(f'Wins: {sum([1 for x in wide_results if x >= 0])}')
print(f'Losses: {sum([1 for x in wide_results if x < 0])}')
print(f'Mean score: {round(statistics.mean(wide_results),2)}')
print(f'Standard deviation (score): {round(statistics.stdev(wide_results),2)}')
print(f'Median score: {round(statistics.median(wide_results),2)}')
