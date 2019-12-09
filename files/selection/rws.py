import numpy as np
from ..helper_funcs.helper import calculate_probability

def roulette_wheel_selection(population):
    """Apply Roulette Wheel Selection method.

    Args:
        population: (list of) plans of the current generation.

    Returns:
        (list of) most fit members of the current population.
    """

    new_mating_pool = []

    calculate_probability(population)

    while(len(new_mating_pool) < len(population)):
        relative_probability = 0.0
        r = np.random.uniform(0, 1)

        for plan in population:
            relative_probability += plan.get_probability()
            if relative_probability >= r:
                new_mating_pool.append(plan)
                break

    return new_mating_pool
