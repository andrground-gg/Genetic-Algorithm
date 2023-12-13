from ga.genetic_algorithm import GeneticAlgorithm
from ga.selection import SelectionMethod
from ga.crossover import CrossoverMethod
from ga.mutation import MutationMethod
import matplotlib.pyplot as plt

def compare_population_sizes(nodes):
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=10, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=200, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0)

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

def compare_selection_methods(nodes, elitism_portion):
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=elitism_portion)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.TOURNAMENT,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=elitism_portion)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.STOCHASTIC_UNIVERSAL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=elitism_portion)

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
    ax.set_title('Elitism portion = ' + str(elitism_portion))
    plt.show()

def compare_crossover_methods(nodes, crossover_rate):
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=crossover_rate,
                        elitism_portion=0)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.TWO_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=crossover_rate,
                        elitism_portion=0)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.UNIFORM,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=crossover_rate,
                        elitism_portion=0)

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
    ax.set_title('Crossover rate = ' + str(crossover_rate))
    plt.show()

def compare_mutation_methods(nodes, mutation_rate):
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=mutation_rate, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SCRAMBLE,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=mutation_rate, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.INVERSION,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=mutation_rate, 
                        crossover_rate=1,
                        elitism_portion=0)

    ga1.run(500)
    ga2.run(500)
    ga3.run(500)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ga1.get_history(), label='Swap mutation')
    ax.plot(ga2.get_history(), label='Scramble mutation')
    ax.plot(ga3.get_history(), label='Inversion mutation')
    ax.set_ylabel('Mean fitness')
    ax.set_xlabel('Generation')
    ax.legend()
    ax.set_title('Mutation rate = ' + str(mutation_rate))
    plt.show()

def compare_elitism_portions(nodes):
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0.1)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0.5)
    
    ga4 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0.75)

    ga1.run(500)
    ga2.run(500)
    ga3.run(500)
    ga4.run(500)


    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ga1.get_history(), label='Elitism portion = 0')
    ax.plot(ga2.get_history(), label='Elitism portion = 0.1')
    ax.plot(ga3.get_history(), label='Elitism portion = 0.5')
    ax.plot(ga4.get_history(), label='Elitism portion = 0.75')
    ax.set_ylabel('Mean fitness')
    ax.set_xlabel('Generation')
    ax.legend()
    plt.show()

def compare_mutation_rates(nodes):
    ga1 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga2 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.01, 
                        crossover_rate=1,
                        elitism_portion=0)
    
    ga3 = GeneticAlgorithm(selection_method=SelectionMethod.ROULETTE_WHEEL,
                        crossover_method=CrossoverMethod.SINGLE_POINT,
                        mutation_method=MutationMethod.SWAP,
                        genes=nodes, 
                        population_size=100, 
                        mutation_rate=0.1, 
                        crossover_rate=1,
                        elitism_portion=0)

    ga1.run(500)
    ga2.run(500)
    ga3.run(500)


    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ga1.get_history(), label='Mutation rate = 0')
    ax.plot(ga2.get_history(), label='Mutation rate = 0.01')
    ax.plot(ga3.get_history(), label='Mutation rate = 0.1')
    ax.set_ylabel('Mean fitness')
    ax.set_xlabel('Generation')
    ax.legend()
    plt.show()