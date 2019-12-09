from .rws import roulette_wheel_selection
from .sus import stochastic_universal_sampling
from .ts import tournament_selection

def selection(population, method):
    """Apply selection method of a given population.

    Args:
        population: (list of) plans to apply the selection on.
        method: (str) selection method:
            - rws (Roulette Wheel Selection)
            - sus (Stochastic Universal Selection)
            - ts  (Tournament Selection)

    Returns:
        (list of) plans representing the new pool
    """

    if method == "rws":
        return roulette_wheel_selection(population)

    elif method == "sus":
        return stochastic_universal_sampling(population)

    elif method == "ts":
        return tournament_selection(population)
