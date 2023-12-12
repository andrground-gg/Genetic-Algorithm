from utils import read_nodes_from_file, generate_nodes, get_total_cost
from selection import SelectionMethod
from crossover import CrossoverMethod
from genetic_algorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

if __name__ == "__main__":
    nodes_from_file = read_nodes_from_file('example.txt')
    nodes = generate_nodes(nodes_from_file)

    ga = GeneticAlgorithm(SelectionMethod.ROULETTE_WHEEL, CrossoverMethod.SINGLE_POINT, nodes, 100, 0.01, 0.7)
    best = ga.run(100)
    print('Best path: ', [node.get_number() for node in best])
    print('Total cost: ', get_total_cost(best))

    plt.plot(ga.get_history())
    plt.ylabel('Mean fitness')
    plt.xlabel('Generation')
    plt.show()
