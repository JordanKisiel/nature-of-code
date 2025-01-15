from evolution.dna import *
from evolution.population import *

POPULATION_SIZE = 1000
TARGET = "it is a truth universally acknowledged that a man in good fortune must be in want of a wife"
GENERATIONS = 100000
MUTATION_RATE = 0.001

def main():
    members = []
    i = 0

    setup(members)

    population = Population(members) 

    while i < GENERATIONS:
        population.calculate_fitness_scores(TARGET)
        best = population.get_best_member()
        if target_found(best):
            break
        print(f'''
              best phrase: {best.genes} 
              fitness: {best.fitness} 
              gen: {i}
              pool size: {len(population.mating_pool)}
              pop size: {len(population.members)}''')
        population.generate_mating_pool()
        population.produce_next_generation(MUTATION_RATE)
        
        i += 1



def target_found(best_member):
    if best_member.fitness == 1.0:
        print(f"target found: {best_member.genes}")
        return True
    return False
                                            
def setup(population):
    for n in range(POPULATION_SIZE):
        population.append(DNA(len(TARGET)))

if __name__ == "__main__":
    main()
