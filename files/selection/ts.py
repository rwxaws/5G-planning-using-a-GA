import copy

import numpy.random as nprandom


def tournament_selection(population):
    """Apply Tournament Selection method.

    Args:
        population: (list of) plans of the current generation.

    Returns:
        (list of) most fit members of the current population.
    """

    old_pool = copy.deepcopy(population)
    new_mating_pool = []

    for _ in range(len(population)):
        f1 = nprandom.choice(old_pool)
        f2 = nprandom.choice(old_pool)

        if f1.get_fitness() >= f2.get_fitness():
            new_mating_pool.append(f1)
        else:
            new_mating_pool.append(f2)
    return new_mating_pool
