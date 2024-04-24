from population import Population
from consts.constants import POPULATION_SIZE
from consts.constants import TARGET_CHROMOSOME
from genetic_algorithm import evolve

from chromosome import Chromosome


def print_population(population: Population, prompt: str) -> None:
    print(prompt)
    print("----------------------------")
    print("{}". \
          format("".join(population.chromosomes.__repr__())))


def main() -> None:
    population = Population(population_length=POPULATION_SIZE)
    population.init_population()
    print("Target word: {}".format(TARGET_CHROMOSOME))
    print_population(population, "Generation # 0")

    generation_number = 0
    print(population.get_max_fitness_chromosome())
    while population.get_max_fitness_chromosome() < len(TARGET_CHROMOSOME):
        generation_number += 1
        population = evolve(population)
        population.sort_chromosome_by_fitness()
        prompt = "Generation #" + str(generation_number)
        print_population(population, prompt=prompt)


main()
