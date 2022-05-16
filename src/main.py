import statistics

from src.a_star_agent import AStarAgent
from src.deep_agent import DeepAgent
from src.dummy_agent import DummyAgent
from src.environment import Environment

import sys

from src.smart_environment import SmartEnvironment
from src.uniform_cost_agent import UniformCostAgent
from src.wide_agent import WideAgent

sys.setrecursionlimit(10000)
def run_with_coverage(agent_class,environmnt_class=Environment):
    stats=[]
    print('--------------------')
    for _ in range(1000):
        env = environmnt_class(_)
        print(f"{_}--> {env.hand}")
        agent = agent_class(env)
        while not env.finish():
            agent.step()
        stats.append(env.score())

    print()
    print(f'---------{agent_class}----------------')
    print(f'Number of samples: {len(stats)}')
    print(f'Wins: {sum([1 for x in stats if x >= 0])}')
    print(f'Losses: {sum([1 for x in stats if x < 0])}')
    print(f'Mean score: {round(statistics.mean(stats), 2)}')
    print(f'Standard deviation (score): {round(statistics.stdev(stats), 2)}')
    print(f'Median score: {round(statistics.median(stats), 2)}')
    print('--------------------')



# run_with_coverage(DummyAgent)
# run_with_coverage(DeepAgent,SmartEnvironment)
# run_with_coverage(WideAgent,SmartEnvironment)
run_with_coverage(AStarAgent,SmartEnvironment)
# run_with_coverage(UniformCostAgent,SmartEnvironment)
