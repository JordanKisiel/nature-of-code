from abc import abstractmethod, ABC
from evolution.dna import *
import random

class Crossover_Strategy(ABC):
    @abstractmethod
    def crossover():
        pass

class Split_Crossover(Crossover_Strategy):
    def __init__(self):
        pass

    def crossover(self, dna, other_dna):
        child = DNA(len(dna.genes), 
                    dna.crossover_strategy)
        child_genes = list(child.genes)
        dna_genes = list(dna.genes)
        other_genes = list(other_dna.genes)

        midpoint = random.randint(0, len(dna.genes))

        for n in range(len(dna.genes)):
            if n < midpoint:
                child_genes[n] = dna_genes[n]
            else:
                child_genes[n] = other_genes[n]

        child.genes = "".join(child_genes)
        
        return child 
    
class Interweave_Crossover(Crossover_Strategy):
    def __init__(self):
        pass

    def crossover(self, dna, other_dna):
        child = DNA(len(dna.genes), 
                    dna.crossover_strategy)
        child_genes = list(child.genes)
        dna_genes = list(dna.genes)
        other_genes = list(other_dna.genes)

        for n in range(len(dna.genes)):
            if random.random() < 0.5:
                child_genes[n] = dna_genes[n]
            else:
                child_genes[n] = other_genes[n]
        
        child.genes = "".join(child_genes)

        return child
        