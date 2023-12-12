from enum import Enum

class SelectionMethod(Enum):
    ROULETTE_WHEEL = 0
    TOURNAMENT = 1
    RANDOM = 2
    ELITIST = 3

class Selection:
    def __init__(self, method, num_parents):
        self.__method = method
        self.__fitnesses = []
        self.__num_parents = num_parents

    def execute(self, fitnesses):
        self.__fitnesses = fitnesses

        if self.__method == SelectionMethod.ROULETTE_WHEEL:
            return self.__roulette_wheel()
        
        if self.__method == SelectionMethod.TOURNAMENT:
            return self.__tournament()
        
        if self.__method == SelectionMethod.RANDOM:
            return self.__random()
        
        if self.__method == SelectionMethod.ELITIST:
            return self.__elitist()
        
        pass

    def __roulette_wheel(self):
        pass

    def __tournament(self):
        pass

    def __random(self):
        pass

    def __elitist(self):
        pass
        