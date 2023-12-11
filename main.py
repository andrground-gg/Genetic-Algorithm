from utils import read_nodes_from_file, generate_nodes, get_total_cost
from genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    nodes_from_file = read_nodes_from_file('example.txt')
    nodes = generate_nodes(nodes_from_file)

    best = GeneticAlgorithm(nodes, 100, 0.01, 0.7).run(100)
    print('Best path: ', [node.get_number() for node in best])
    print('Total cost: ', get_total_cost(best))
