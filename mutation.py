from enum import Enum
import random

class MutationMethod(Enum):
    SWAP = 0
    SCRAMBLE = 1
    INVERSION = 2

class Mutation:
    def __init__(self, method, mutation_rate):
        self.__method = method
        self.__mutation_rate = mutation_rate
        self.__offspring = []

    def execute(self, offspring):
        self.__offspring = offspring

        if random.random() < self.__mutation_rate:
            if self.__method == MutationMethod.SWAP:
                return self.__swap()
            
            if self.__method == MutationMethod.SCRAMBLE:
                return self.__scramble()
            
            if self.__method == MutationMethod.INVERSION:
                return self.__inversion()
        
        return offspring.copy()

    def __swap(self):
        index1, index2 = random.sample(range(len(self.__offspring)), 2)
        self.__offspring[index1], self.__offspring[index2] = self.__offspring[index2], self.__offspring[index1]
        return self.__offspring

    def __scramble(self):
        start = random.randint(0, len(self.__offspring))
        end = random.randint(start, len(self.__offspring))
        genes = self.__offspring[start:end]
        random.shuffle(genes)
        self.__offspring[start:end] = genes
        
        return self.__offspring

    def __inversion(self):
        start = random.randint(0, len(self.__offspring))
        end = random.randint(start, len(self.__offspring))
        genes = self.__offspring[start:end]
        genes.reverse()
        self.__offspring[start:end] = genes

        return self.__offspring