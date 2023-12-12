import random
import numpy as np
from utils import get_total_cost
from selection import Selection
from crossover import Crossover
from mutation import Mutation

class GeneticAlgorithm:
    def __init__(self, selection_method, crossover_method, mutation_method, genes, population_size, mutation_rate, crossover_rate, elitism_portion=0):
        self.__selection = Selection(selection_method, 2)
        self.__crossover = Crossover(crossover_method, crossover_rate)
        self.__mutation = Mutation(mutation_method, mutation_rate)
        self.__mutation_rate = mutation_rate
        self.__crossover_rate = crossover_rate
        self.__elitism_portion = elitism_portion
        self.__population_size = population_size
        self.__population = self.__init_population(population_size, genes)
        self.__history = []
        
    def get_history(self):
        return self.__history
    
    def __init_population(self, population_size, genes):
        population = []
        for i in range(population_size):
            genes_copy = genes.copy()
            random.shuffle(genes_copy)
            population.append(genes_copy)

        return population
    
    def __calculate_fitness(self, individual):
        return get_total_cost(individual)
    
    def __calculate_fitnesses(self):
        return [self.__calculate_fitness(individual) for individual in self.__population]
    
    def __select_parents(self, fitness_values):
        return self.__selection.execute(fitness_values, self.__population)
    
    def __execute_crossover(self, parent1, parent2):
        return self.__crossover.execute(parent1, parent2)
            
    def __execute_mutation(self, individual):
        return self.__mutation.execute(individual)
    
    def run(self, num_generations):
        for gen in range(num_generations):
            new_population = []

            if self.__elitism_portion > 0:
                num_elites = int(self.__elitism_portion * self.__population_size)
                elites = sorted(self.__population, key=self.__calculate_fitness)[:num_elites]
                new_population.extend(elites)

            for _ in range(self.__population_size - len(new_population)):
                parent1, parent2 = self.__select_parents(self.__calculate_fitnesses())

                child1 = self.__execute_crossover(parent1, parent2)
                child2 = self.__execute_crossover(parent2, parent1)
                
                child1 = self.__execute_mutation(child1)
                child2 = self.__execute_mutation(child2)

                new_population.extend([child1, child2])

            self.__population = new_population
            self.__history.append(np.mean(self.__calculate_fitnesses()))

            if gen % 50 == 0:
                print('Generation: ', gen, ' Mean fitness: ', self.__history[-1])

        return min(self.__population, key=self.__calculate_fitness)