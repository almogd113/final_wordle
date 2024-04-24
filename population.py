from chromosome import Chromosome


class Population:
    def __init__(self, population_length: int):
        self.chromosomes = []
        self.population_length = population_length

    def init_population(self) -> None:
        for index in range(self.population_length):
            chromosome_to_insert = Chromosome()
            chromosome_to_insert.genes_init()
            self.chromosomes.append(chromosome_to_insert)
        self.sort_chromosome_by_fitness()

    def get_max_fitness_chromosome(self) -> int:
        return self.chromosomes[0].calculate_fitness()

    def sort_chromosome_by_fitness(self) -> None:
        self.chromosomes = sorted(self.chromosomes, key=lambda chromosome: chromosome.get_fitness(), reverse=True)
