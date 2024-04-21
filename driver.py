from population import Population
from consts.constants import POPULATION_SIZE
from consts.constants import TARGET_CHROMOSOME
from chromosome import Chromosome


def print_population(population: Population, prompt: str) -> None:
    print(prompt)
    print("----------------------------")
    print("{}" . \
          format("".join(population.chromosomes.__repr__())))


def main() -> None:
    population = Population(population_length=POPULATION_SIZE)
    print_population(population, "print population")


main()
