from chromosome import Chromosome


class Population:
    def __init__(self, population_length: int):
        self.chromosomes = []
        self.population_length = population_length
        self.init_population()

    def init_population(self) -> None:
        for index in range(self.population_length):
            self.chromosomes.append(Chromosome())
        self.sort_chromosome_by_fitness()

    def sort_chromosome_by_fitness(self) -> None:
        self.chromosomes = sorted(self.chromosomes, key=lambda chromosome: chromosome.get_fitness())
