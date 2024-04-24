from population import Population
from consts.constants import POPULATION_SIZE
from consts.constants import TOURNAMENT_SELECTION_SIZE
from chromosome import Chromosome
from consts.constants import NUMBER_OF_ELITE_CHROMOSOMES
from consts.constants import MUTATION_RATE
import random


def crossover_population(population: Population) -> Population:
    population_crossover = Population(len(population.chromosomes))
    for index in range(NUMBER_OF_ELITE_CHROMOSOMES):
        population_crossover.chromosomes.append(population.chromosomes[index])

    for index in range(1, len(population.chromosomes)):
        # getting the fittest chromosome to be parents
        parent_1 = select_tournament_population(population).chromosomes[0]
        parent_2 = select_tournament_population(population).chromosomes[0]
        child = crossover_chromosome(parent_1, parent_2)
        population_crossover.chromosomes.append(child)
    return population_crossover


def crossover_chromosome(chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
    crossover_chromosome_object = Chromosome()
    for index in range(len(chromosome1.genes)):
        if random.randrange(0, 2) > 0.5:
            crossover_chromosome_object.genes.append(chromosome1.genes[index])
        else:
            crossover_chromosome_object.genes.append(chromosome2.genes[index])
    return crossover_chromosome_object


def select_tournament_population(population: Population) -> Population:
    tournament_population = Population(TOURNAMENT_SELECTION_SIZE)
    for index in range(TOURNAMENT_SELECTION_SIZE):
        index_to_insert = random.randrange(0, len(population.chromosomes))
        tournament_population.chromosomes.append(population.chromosomes[index_to_insert])
    tournament_population.sort_chromosome_by_fitness()
    return tournament_population


def mutate_population(population: Population) -> Population:
    population_mutate = Population(POPULATION_SIZE)
    for index in range(NUMBER_OF_ELITE_CHROMOSOMES):
        population_mutate.chromosomes.append(population.chromosomes[index])

    for index in range(NUMBER_OF_ELITE_CHROMOSOMES, len(population.chromosomes)):
        chromosome_to_mutate = population.chromosomes[index]
        population_mutate.chromosomes.append(mutate_chromosome(chromosome_to_mutate))
    return population_mutate


def mutate_chromosome(chromosome: Chromosome) -> Chromosome:
    chromosome_mutate = Chromosome()
    for index in range(len(chromosome.genes)):
        if random.randrange(0, 2) < MUTATION_RATE:
            chromosome_mutate.genes.append(random.choice(chromosome.VALID_GENES_LIST))

        else:
            chromosome_mutate.genes.append(chromosome.genes[index])

    return chromosome_mutate


def evolve(population: Population) -> Population:
    return mutate_population(crossover_population(population))
