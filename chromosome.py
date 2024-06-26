import random
from consts.constants import TARGET_CHROMOSOME
from consts.constants import VALID_GENES


class Chromosome:
    VALID_GENES_LIST = list(VALID_GENES)
    is_fitness_changed = False

    def __init__(self):
        self.target_word = TARGET_CHROMOSOME
        self.genes = []
        self.fitness = 0

    def genes_init(self) -> None:
        for x in range(len(TARGET_CHROMOSOME)):
            self.genes.append(random.choice(self.VALID_GENES_LIST))

    def calculate_fitness(self) -> int:
        fitness_count = 0
        for gene_target, gene_chromosome in zip(self.target_word, self.genes):
            if gene_target == gene_chromosome:
                fitness_count += 1
        return fitness_count

    def get_fitness(self) -> int:
        # if self.is_fitness_changed:
        self.fitness = self.calculate_fitness()
        # self.is_fitness_changed = False
        return self.fitness

    def genes_string(self) -> str:
        return "".join(self.genes)

    def __repr__(self) -> str:
        format_txt = "Genes: {}\t fitness: {}\n"
        return format_txt.format("".join(self.genes_string()), self.calculate_fitness())

# def print_list(lst: []) -> None:
#     for x in lst:
#         print(x)


# print_list(Chromosome(5).)
# Chromosome().chromosome_string()
