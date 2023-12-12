from utils import read_nodes_from_file, generate_nodes, get_total_cost
from selection import SelectionMethod
from crossover import CrossoverMethod
from mutation import MutationMethod
from genetic_algorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

def compare_crossover_methods():
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.TWO_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.UNIFORM,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)

    ga1.run(500)
    ga2.run(500)
    ga3.run(500)


    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ga1.get_history(), label='Single point crossover')
    ax.plot(ga2.get_history(), label='Two point crossover')
    ax.plot(ga3.get_history(), label='Uniform crossover')
    ax.set_ylabel('Mean fitness')
    ax.set_xlabel('Generation')
    ax.legend()
    plt.show()

def compare_population_sizes():
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=10, 
                        mutation_rate=0.01, 
                        crossover_rate=1)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=200, 
                        mutation_rate=0.01, 
                        crossover_rate=1)

    ga1.run(500)
    ga2.run(500)
    ga3.run(500)


    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ga1.get_history(), label='Population size = 50')
    ax.plot(ga2.get_history(), label='Population size = 100')
    ax.plot(ga3.get_history(), label='Population size = 200')
    ax.set_ylabel('Mean fitness')
    ax.set_xlabel('Generation')
    ax.legend()
    plt.show()

def compare_selection_methods():
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.TOURNAMENT,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.STOCHASTIC_UNIVERSAL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1)

    ga1.run(500)
    ga2.run(500)
    ga3.run(500)


    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ga1.get_history(), label='Roulette wheel selection')
    ax.plot(ga2.get_history(), label='Tournament selection')
    ax.plot(ga3.get_history(), label='Stochastic universal selection')
    ax.set_ylabel('Mean fitness')
    ax.set_xlabel('Generation')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    nodes_from_file = read_nodes_from_file('example.txt')
    nodes = generate_nodes(nodes_from_file)

    # compare_crossover_methods()
    # compare_population_sizes()
    compare_selection_methods()
