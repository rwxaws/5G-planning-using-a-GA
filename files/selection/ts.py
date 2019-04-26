import copy

import numpy.random as nprandom


def tournament_selection(population):
    old_pool = copy.deepcopy(population)
    new_pool = []

    for _ in range(len(population)):
        f1 = nprandom.choice(old_pool)
        f2 = nprandom.choice(old_pool)

        if f1.get_fitness() >= f2.get_fitness():
            new_pool.append(f1)
        else:
            new_pool.append(f2)
    return new_pool
