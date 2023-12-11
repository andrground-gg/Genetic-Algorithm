import random
from utils import get_total_cost

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.__mutation_rate = mutation_rate
        self.__crossover_rate = crossover_rate
        self.__population = self.__init_population(population_size)
        
    def __init_population(self, population_size, genes):
        population = []
        for i in range(population_size):
            random.shuffle(genes)
            population.append(genes)

        return population
    
    def calculate_fitness(self, individual):
        return get_total_cost(individual)