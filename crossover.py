from enum import Enum
import random

import numpy as np

class CrossoverMethod(Enum):
    SINGLE_POINT = 0
    TWO_POINT = 1
    UNIFORM = 2

class Crossover:
    def __init__(self, method, crossover_rate):
        self.__method = method
        self.__crossover_rate = crossover_rate
        self.__parent1 = []
        self.__parent2 = []

    def execute(self, parent1, parent2):
        self.__parent1 = parent1
        self.__parent2 = parent2

        if random.random() < self.__crossover_rate:
            if self.__method == CrossoverMethod.SINGLE_POINT:
                return self.__single_point()
            
            if self.__method == CrossoverMethod.TWO_POINT:
                return self.__two_point()
            
            if self.__method == CrossoverMethod.UNIFORM:
                return self.__uniform()
        
        return parent1.copy()

    def __single_point(self):
        crossover_point = random.randint(0, len(self.__parent1))
        return self.__parent1[:crossover_point] + [gene for gene in self.__parent2 if gene not in self.__parent1[:crossover_point]]

    def __two_point(self):
        crossover_point1 = random.randint(0, len(self.__parent1))
        crossover_point2 = random.randint(0, len(self.__parent1))

        if crossover_point1 > crossover_point2:
            crossover_point1, crossover_point2 = crossover_point2, crossover_point1

        return self.__parent1[:crossover_point1] + [gene for gene in self.__parent2 if gene not in self.__parent1[:crossover_point1] and gene not in self.__parent1[crossover_point2:]] + self.__parent1[crossover_point2:]

    def __uniform(self):
        child = [None] * len(self.__parent1)
        remaining_genes = set(self.__parent1)

        for i in range(len(self.__parent1)):
            parent = self.__parent1 if random.random() < 0.5 else self.__parent2
            if parent[i] not in child:
                child[i] = parent[i]
                remaining_genes.remove(parent[i])

        for i in range(len(child)):
            if child[i] is None:
                child[i] = remaining_genes.pop()

        return child