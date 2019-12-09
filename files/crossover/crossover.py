import copy

import numpy as np

from .simple_arithmetic_crossover import simple_arithmetic_crossover
from .single_arithmetic_crossover import single_arithmetic_crossover
from .whole_arithmetic_crossover import whole_arithmetic_crossover


def crossover(pool, crossover_probability, crosspoint, crossover_method, alpha):
    """Apply crossover method on given pool of plans.

    Args:
        pool: (list of) plans obj.
        crossover_probability: (int).
        crosspoint: (int) should be a randomly generated number.
        crossover_method: (str) must be one of the following:
            - simple_arithmetic
            - single_arithmetic
            - whole_arithmetic
        alpha: (int) used to calculate the values in simple_arithmetic and single_arithmetic.
    
    Returns:
        (list of) plans
    """

    new_pool = []

    # each crossover generates 2 offspring
    num_children = len(pool) // 2

    for _ in range(num_children):
        parent1 = np.random.choice(pool)
        parent2 = np.random.choice(pool)
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        num_cells_non_fixed = len(parent1.get_cells("non_fixed"))
        if crossover_method == "simple_arithmetic":
            for i in range(crosspoint + 1, num_cells_non_fixed):
                simple_arithmetic_crossover(child1.get_cells("non_fixed")[i],
                                            child2.get_cells("non_fixed")[i],
                                            alpha)

        elif crossover_method == "single_arithmetic":
            single_arithmetic_crossover(child1, child2, alpha)

        elif crossover_method == "whole_arithmetic":
            for i in range(num_cells_non_fixed):
                whole_arithmetic_crossover(child1.get_cells("non_fixed")[i],
                                           child2.get_cells("non_fixed")[i],
                                           alpha)

        new_pool.append(child1)
        new_pool.append(child2)

    return new_pool
