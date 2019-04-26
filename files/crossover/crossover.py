import copy

import numpy as np

from .simple_arithmetic_crossover import simple_arithmetic_crossover
from .single_arithmetic_crossover import single_arithmetic_crossover

def crossover(pool, crossover_probability, crosspoints, crossover_method, alpha):
    new_pool = []

    # each crossover generates 2 offspring
    num_children = len(pool) // 2

    for _ in range(num_children):
        parent1 = np.random.choice(pool)
        parent2 = np.random.choice(pool)
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        num_cells = len(parent1.get_cells("non_fixed"))
        for i in range(num_cells):

            random_number = round(np.random.random(), 3)
            if random_number <= crossover_probability:
                if crossover_method == "simple_arithmetic":
                    simple_arithmetic_crossover(child1.get_cells("non_fixed")[i],
                                                child2.get_cells("non_fixed")[i],
                                                alpha)
                elif crossover_method == "single_arithmetic":
                    single_arithmetic_crossover(child1, child2)
                else:
                    pass
        new_pool.append(child1)
        new_pool.append(child2)

    return new_pool
