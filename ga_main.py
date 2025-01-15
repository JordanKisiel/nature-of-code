from evolution.dna import *
from evolution.population import *
from evolution.crossover import *
from evolution.fitness import *

POPULATION_SIZE = 1000
TARGET = "it is a truth universally acknowledged that a man in good fortune must be in want of a wife"
GENERATIONS = 100000
MUTATION_RATE = 0.01
crossover_strat = Interweave_Crossover()
adj_strat = Rank_Adjust()

def main():
    members = []
    i = 0

    setup(members)

    population = Population(members, adj_strat) 

    highest_fitness = 0

    while i < GENERATIONS:
        population.calculate_raw_fitness_scores(TARGET)
        population.sort()
        population.rank()
        best = population.get_best_member()
        if best.raw_fitness > highest_fitness:
            highest_fitness = best.raw_fitness
        if target_found(best):
            break
        print(f'''
              best phrase: {best.genes} 
              fitness: {best.raw_fitness} 
              highest fitness: {highest_fitness}
              gen: {i}
              pool size: {len(population.mating_pool)}
              avg pool fitness: {population.get_avg_mating_fitness()}
              pop size: {len(population.members)}''')
        population.adjust_fitness_scores()
        population.generate_mating_pool()
        population.produce_next_generation(MUTATION_RATE)
        
        i += 1



def target_found(best_member):
    if best_member.raw_fitness == 1.0:
        print(f"target found: {best_member.genes}")
        return True
    return False
                                            
def setup(population):
    for n in range(POPULATION_SIZE):
        member = DNA(len(TARGET), 
                     crossover_strat)
        population.append(member)

if __name__ == "__main__":
    main()
