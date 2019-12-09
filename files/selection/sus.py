import numpy as np
from ..helper_funcs.helper import calculate_probability

def stochastic_universal_sampling(population):
    """Apply Stochastic Universal Selection method.

    Args:
        population: (list of) plans of the current generation.

    Returns:
        (list of) most fit members of the current population.
    """

    new_mating_pool = []

    calculate_probability(population)
    r = np.random.uniform(0, 1 / len(population))
    relative_probability = 0.0
    current_member = 0

    while(len(new_mating_pool) < len(population)):
        relative_probability += population[current_member].get_probability()

        while(r <= relative_probability):
            new_mating_pool.append(population[current_member])
            r += 1 / len(population)

            current_member += 1

    return new_mating_pool
