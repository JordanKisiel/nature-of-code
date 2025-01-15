from evolution.dna import *
import random
import math

class Population:
    def __init__(self, members, adj_strat):
        self.size = len(members)
        self.members = members
        self.mating_pool = []
        self.adj_strat = adj_strat

    def calculate_raw_fitness_scores(self, target):
        for member in self.members:
            raw_fit = 0
            for n in range(len(target)):
                if member.genes[n] == target[n]:
                    raw_fit += 1

            member.raw_fitness = raw_fit / len(target)

    def adjust_fitness_scores(self):
        for member in self.members:
            member.adj_fitness = self.adj_strat.adj_fitness(member)

    def generate_mating_pool(self):
        self.mating_pool = []
        for member in self.members:
            num_copies = math.floor(member.adj_fitness * 100)
            for n in range(num_copies):
                self.mating_pool.append(member)

    def get_avg_mating_fitness(self):
        if len(self.mating_pool) == 0:
            return 0
        mating_fitnesses = [member.raw_fitness for member in self.mating_pool]
        fit_sum = sum(mating_fitnesses)
        return fit_sum / len(self.mating_pool)

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

    def sort(self):
        self.members.sort(key=lambda x: x.raw_fitness, reverse=True)

    def rank(self):
        for index, member in enumerate(self.members):
            member.rank = index + 1

    def get_best_member(self):
        return self.members[0]
    
    def print_mating_pool(self):
        for parent in self.mating_pool:
            print(parent.genes)

    def print(self):
        self.sort()
        for index, member in enumerate(self.members):
            print(f'''
                  genes: {member.genes}
                  rank: {index + 1}
                  fitness: {member.raw_fitness}''')
            
    def print_n_best(self, num):
        self.sort()
        for index, member in enumerate(self.members):
            if index < num:
                print(f'''
                    genes: {member.genes}
                    rank: {index + 1}
                    fitness: {member.raw_fitness}''')
    
