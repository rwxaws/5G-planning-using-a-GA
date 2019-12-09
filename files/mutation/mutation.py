import numpy as np

from .non_uniform_mutation import non_uniform_mutation
from .uniform_mutation import uniform_mutation


def mutation(pool, area, probability, method, dist="cauchy"):
    """Apply mutation over the whole pool.

    Args:
        pool: (list of) plans to apply mutation over.
        area: (int) area of interest.
        probability: (int) probability of mutation.
        method: (str) mutation method.
            - uniform
            - non_uniform
        dist: (str) type of distribution to be used (needed only in non_uniform_mutation).
            - cauchy (default)
            - gaussian

    Returns:
        None
    """

    for plan in pool:
        # apply for non_fixed cells only.
        for cell in plan.get_cells("non_fixed"):
            random_number = np.random.random()
            if random_number <= probability:
                if method == "uniform":
                    uniform_mutation(cell, area)
                elif method == "non_uniform":
                    non_uniform_mutation(cell, area, dist)
