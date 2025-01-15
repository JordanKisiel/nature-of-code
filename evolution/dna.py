import random
import string
import math

class DNA:
    def __init__(self, length):
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet.append(" ")
        self.genes = self._initilize_dna(length)
        self.fitness = 0

    def _initilize_dna(self, length):
        rand_str = ""
        for n in range(length):
            rand_str += self.alphabet[random.randint(0, 26)]
        
        return rand_str
    
    def calculate_fitness(self, target):
        raw_fit = 0
        for n in range(len(target)):
            if self.genes[n] == target[n]:
                raw_fit += 1

        self.fitness = raw_fit / len(target)
    
    def crossover(self, other_dna):
        child = DNA(len(self.genes))
        child_genes = list(child.genes)
        self_genes = list(self.genes)
        other_genes = list(other_dna.genes)

        midpoint = random.randint(0, len(self.genes))

        for n in range(len(self.genes)):
            if n < midpoint:
                child_genes[n] = self_genes[n]
            else:
                child_genes[n] = other_genes[n]

        child.genes = "".join(child_genes)
        
        return child

    def mutate(self, mutation_rate):
        self_genes = list(self.genes)
        for index, gene in enumerate(self.genes):
            if random.random() < mutation_rate:
                rand_index = random.randint(0, len(self.alphabet) - 1)
                self_genes[index] = self.alphabet[rand_index]
        
        self.genes = "".join(self_genes)
        