from enum import Enum
import random

class MutationMethod(Enum):
    RANDOM = 0
    SWAP = 1
    SCRAMBLE = 2
    INVERSION = 3

class Mutation:
    def __init__(self, method, mutation_rate):
        self.__method = method
        self.__mutation_rate = mutation_rate
        self.__offspring = []

    def execute(self, offspring):
        self.__offspring = offspring

        if random.random() < self.__mutation_rate:
            if self.__method == MutationMethod.RANDOM:
                return self.__random()
            
            if self.__method == MutationMethod.SWAP:
                return self.__swap()
            
            if self.__method == MutationMethod.SCRAMBLE:
                return self.__scramble()
            
            if self.__method == MutationMethod.INVERSION:
                return self.__inversion()
        
        return offspring.copy()

    def __random(self):
        pass

    def __swap(self):
        pass

    def __scramble(self):
        pass

    def __inversion(self):
        pass