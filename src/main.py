import datetime
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


def run_with_coverage(agent_class, environmnt_class=Environment):
    scores = []
    visited_nodes = []
    times = []
    lost_agents = 0
    print('--------------------')
    for _ in range(1000):
        env = environmnt_class(_)
        print(_)
        agent = agent_class(env)
        start = datetime.datetime.now()
        while not env.finish() and not agent.lost:
            agent.step()
        if agent.lost:
            lost_agents += 1
        end = datetime.datetime.now()
        scores.append(env.score())
        times.append((end - start).total_seconds())
        if hasattr(agent, 'graph'):
            visited_nodes.append(len(agent.graph.visited_nodes))

    print()
    print(f'---------{agent_class}----------------')
    print(f'Number of samples: {len(scores)}')
    print(f'Wins: {sum([1 for x in scores if x >= 0])}')
    print(f'Losses: {sum([1 for x in scores if x < 0])}')
    print(f'Mean score: {round(statistics.mean(scores), 2)}')
    print(f'Standard deviation (score): {round(statistics.stdev(scores), 2)}')
    print(f'Median score: {round(statistics.median(scores), 2)}')
    if visited_nodes:
        print(f'Mean visited nodes: {round(statistics.mean(visited_nodes), 2)}')
        print(f'Standard visited nodes: {round(statistics.stdev(visited_nodes), 2)}')
        print(f'Median visited nodes: {round(statistics.median(visited_nodes), 2)}')

    print(f'Mean execution time: {statistics.mean(times)}')
    print(f'Standard execution time: {statistics.stdev(times)}')
    print(f'Median execution time: {statistics.median(times)}')
    print('--------------------')

    print(f'Los agents: {lost_agents}')




run_with_coverage(DummyAgent)
run_with_coverage(DeepAgent, SmartEnvironment)
# run_with_coverage(WideAgent,SmartEnvironment)
run_with_coverage(AStarAgent, SmartEnvironment)
# run_with_coverage(UniformCostAgent,SmartEnvironment)
