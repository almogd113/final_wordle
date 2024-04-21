from population import Population


def crossover_population(population: Population) -> Population:
    return population


def mutate_population(population: Population) -> Population:
    return population


def evolve(population: Population) -> Population:
    return mutate_population(crossover_population(population))
