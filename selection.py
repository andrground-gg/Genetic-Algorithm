from enum import Enum
import random

import numpy as np

class SelectionMethod(Enum):
    ROULETTE_WHEEL = 0
    TOURNAMENT = 1
    RANK = 2

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
        
        if self.__method == SelectionMethod.RANK:
            return self.__rank()
        
        pass

    def __roulette_wheel(self):
        fitness_values = np.array(self.__fitnesses)
        scaled_fitness = np.max(fitness_values) - fitness_values
        w = scaled_fitness / np.sum(scaled_fitness)
        indices = random.choices(range(len(self.__population)), k=self.__num_parents, weights=w)
        return [self.__population[index] for index in indices]

    def __tournament(self):
        parents = []
        for _ in range(self.__num_parents):
            random_indices = random.sample(range(len(self.__population)), 2)
            fitnesses = [self.__fitnesses[index] for index in random_indices]
            parents.append(self.__population[random_indices[np.argmin(fitnesses)]])

        return parents

    def __rank(self):
        ranked_indices = np.argsort(self.__fitnesses)
        ranks = np.empty_like(ranked_indices)
        ranks[ranked_indices[::-1]] = np.arange(len(self.__fitnesses)) + 1

        w = ranks / np.sum(ranks)
        indices = random.choices(ranked_indices, k=self.__num_parents, weights=w)
        return [self.__population[index] for index in indices]