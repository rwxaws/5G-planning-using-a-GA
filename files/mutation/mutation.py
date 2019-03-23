import numpy as np

from .non_uniform_mutation import non_uniform_mutation
from .uniform_mutation import uniform_mutation


def mutation(pool, area, probabilty, method, dist="cauchy"):
    """Apply mutation over the whole pool.

    Args:
        pool: Population pool.
        area: Area of interest.
        probabilty: Probabilty of mutation.
        method: Mutation method (uniform, non_uniform).
        dist: Type of distribution to be used in non_uniform mutation.

    Returns:
        None
    """

    for plan in pool:
        # apply for non_fixed cells only.
        for cell in plan.get_cells("non_fixed"):
            random_number = np.random.random()
            if random_number <= probabilty:
                if method == "uniform":
                    uniform_mutation(cell, area)
                elif method == "non_uniform":
                    non_uniform_mutation(cell, dist)