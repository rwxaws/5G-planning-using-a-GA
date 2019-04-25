import numpy.random as nprandom
import copy


def tournament_selection(pool):
    old_pool = copy.deepcopy(pool)
    new_pool = []

    for _ in range(len(pool)):
        f1 = nprandom.choice(old_pool)
        f2 = nprandom.choice(old_pool)

        if f1.get_fitness() >= f2.get_fitness():
            new_pool.append(f1)
        else:
            new_pool.append(f2)
    return new_pool
