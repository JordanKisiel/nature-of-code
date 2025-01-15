from evolution.dna import *
import random

class Population:
    def __init__(self, members):
        self.size = len(members)
        self.members = members
        self.mating_pool = []

    def calculate_fitness_scores(self, target):
        for member in self.members:
            member.calculate_fitness(target)

    def generate_mating_pool(self):
        self.mating_pool = []
        for member in self.members:
            num_copies = math.floor(member.fitness * 100)
            for n in range(num_copies):
                self.mating_pool.append(member)

    def select_parents(self):
        rand_int_1 = random.randint(0, 
                                    len(self.mating_pool) - 1)
        rand_int_2 = random.randint(0, 
                                    len(self.mating_pool) - 1)

        parent_1 = self.mating_pool[rand_int_1]
        parent_2 = self.mating_pool[rand_int_2]

        return (parent_1, parent_2)
    
    def produce_next_generation(self, mutation_rate):
        for n in range(self.size):
            parents = self.select_parents()
            child = parents[0].crossover(parents[1])
            child.mutate(mutation_rate)
            self.members[n] = child

    def sort_population(self):
        self.members.sort(key=lambda x: x.fitness, reverse=True)

    def get_best_member(self):
        self.sort_population()
        return self.members[0]
    
    def print_mating_pool(self):
        for parent in self.mating_pool:
            print(parent.genes)

    def print(self):
        self.sort_population()
        for index, member in enumerate(self.members):
            print(f'''
                  genes: {member.genes}
                  rank: {index + 1}
                  fitness: {member.fitness}''')
            
    def print_n_best(self, num):
        self.sort_population()
        for index, member in enumerate(self.members):
            if index < num:
                print(f'''
                    genes: {member.genes}
                    rank: {index + 1}
                    fitness: {member.fitness}''')
    
