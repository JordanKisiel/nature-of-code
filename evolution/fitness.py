from abc import abstractmethod, ABC

class Adj_Strategy(ABC):
    @abstractmethod
    def adj_fitness():
        pass

class No_Adjust(Adj_Strategy):
    def __init__(self):
        pass

    def adj_fitness(self, dna):
        return dna.raw_fitness

class Rank_Adjust(Adj_Strategy):
    def __init__(self):
        pass

    def adj_fitness(self, dna):
        adj_fitness = 1 / (dna.rank)

        return adj_fitness



 