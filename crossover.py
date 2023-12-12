from enum import Enum
import random

class CrossoverMethod(Enum):
    SINGLE_POINT = 0
    TWO_POINT = 1
    UNIFORM = 2

class Crossover:
    def __init__(self, method, crossover_rate, num_offsprings):
        self.__method = method
        self.__crossover_rate = crossover_rate
        self.__num_offsprings = num_offsprings
        self.__parent1 = None
        self.__parent2 = None

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
        
        return parent1.copy(), parent2.copy()

    def __single_point(self):
        pass

    def __two_point(self):
        pass

    def __uniform(self):
        pass