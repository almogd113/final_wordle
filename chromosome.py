import random
from genetic_algorithm import TARGET_CHROMOSOME


class Chromosome:
    VALID_GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    VALID_GENES_LIST = list(VALID_GENES)
    is_fitness_changed = False

    def __init__(self):
        self.genes = []
        self.fitness = 0
        self.target_word_length = len(TARGET_CHROMOSOME)

        self.genes_init()

    def genes_init(self) -> None:
        for x in range(self.target_word_length):
            self.genes.append(random.choice(self.VALID_GENES_LIST))

    def calculate_fitness(self) -> int:
        fitness_count = 0
        target_chromosome = TARGET_CHROMOSOME
        for gene_target, gene_chromosome in zip(self.genes, target_chromosome):
            if gene_target == gene_chromosome:
                fitness_count += 1
        return fitness_count

    def get_genes(self) -> []:
        self.is_fitness_changed = True
        return self.genes

    def get_fitness(self) -> int:
        if self.is_fitness_changed:
            self.fitness = self.calculate_fitness()
            self.is_fitness_changed = False
        return self.fitness

    def genes_string(self) -> str:
        string_genes = ""
        for x in self.genes:
            string_genes += x
        return string_genes

    def chromosome_string(self) -> None:
        format_txt = "Genes: {}\tfitness: {}"
        print(format_txt.format(self.genes_string(), self.fitness))


# def print_list(lst: []) -> None:
#     for x in lst:
#         print(x)


# print_list(Chromosome(5).)
# Chromosome().chromosome_string()
