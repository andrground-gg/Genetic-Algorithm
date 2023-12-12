from enum import Enum
import random

import numpy as np

class SelectionMethod(Enum):
    ROULETTE_WHEEL = 0
    TOURNAMENT = 1
    STOCHASTIC_UNIVERSAL = 2

class Selection:
    def __init__(self, method, num_parents):
        self.__method = method
        self.__fitnesses = []
        self.__population = []
        self.__num_parents = num_parents

    def execute(self, fitnesses, population):
        self.__fitnesses = fitnesses.copy()
        self.__population = population.copy()

        if self.__method == SelectionMethod.ROULETTE_WHEEL:
            return self.__roulette_wheel()
        
        if self.__method == SelectionMethod.TOURNAMENT:
            return self.__tournament()
        
        if self.__method == SelectionMethod.STOCHASTIC_UNIVERSAL:
            return self.__stochastic_universal()
        
        pass

    def __roulette_wheel(self):
        parents = []
        for _ in range(self.__num_parents):
            fitness_values = np.array(self.__fitnesses)
            scaled_fitness = np.max(fitness_values) - fitness_values + 1e-10
            w = scaled_fitness / np.sum(scaled_fitness)
            indices = random.choices(range(len(self.__population)), k=1, weights=w)
            parents.append(self.__population[indices[0]])

        return parents

    def __tournament(self):
        parents = []
        for _ in range(self.__num_parents):
            random_indices = random.sample(range(len(self.__population)), 2)
            fitnesses = [self.__fitnesses[index] for index in random_indices]
            parents.append(self.__population[random_indices[np.argmin(fitnesses)]])

        return parents

    def __stochastic_universal(self):
        fitness_values = np.array(self.__fitnesses)
        scaled_fitness = np.max(fitness_values) - fitness_values + 1e-10
        weights = scaled_fitness / np.sum(scaled_fitness)

        cumulative_weights = np.cumsum(weights)

        start_point = random.uniform(0, 1 / self.__num_parents)

        pointers = [start_point + i / self.__num_parents for i in range(self.__num_parents)]
        selected_indices = [np.argmax(cumulative_weights >= p) for p in pointers]

        return [self.__population[index] for index in selected_indices]