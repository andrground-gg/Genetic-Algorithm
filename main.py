from tsp.utils import read_nodes_from_file, generate_nodes
from comparisons import compare_population_sizes, compare_selection_methods, compare_crossover_methods, compare_mutation_methods, compare_elitism_portions, compare_mutation_rates

if __name__ == "__main__":
    nodes_from_file = read_nodes_from_file('example.txt')
    nodes = generate_nodes(nodes_from_file)

    # compare_population_sizes(nodes)
    # compare_selection_methods(nodes, 0)
    # compare_selection_methods(nodes, 0.1)
    # compare_selection_methods(nodes, 0.5)
    # compare_crossover_methods(nodes, 1)
    # compare_mutation_methods(nodes, 0)
    # compare_mutation_methods(nodes, 0.01)
    # compare_mutation_methods(nodes, 0.1)
    # compare_elitism_portions(nodes)
    # compare_mutation_rates(nodes)
    

