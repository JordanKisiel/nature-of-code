import random
import string

class DNA:
    def __init__(self, 
                 length, 
                 crossover_strategy):
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet.append(" ")
        self.genes = self._initilize_dna(length)
        self.raw_fitness = 0
        self.adj_fitness = 0
        self.rank = 1
        self.crossover_strategy = crossover_strategy 

    def _initilize_dna(self, length):
        rand_str = ""
        for n in range(length):
            rand_str += self.alphabet[random.randint(0, 26)]
        
        return rand_str
    
    def crossover(self, other_dna):
        child = self.crossover_strategy.crossover(self, 
                                                  other_dna)
        
        return child

    def mutate(self, mutation_rate):
        self_genes = list(self.genes)
        for index, gene in enumerate(self.genes):
            if random.random() < mutation_rate:
                rand_index = random.randint(0, len(self.alphabet) - 1)
                self_genes[index] = self.alphabet[rand_index]
        
        self.genes = "".join(self_genes)