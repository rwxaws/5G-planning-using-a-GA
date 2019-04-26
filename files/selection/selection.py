from .rws import roulette_wheel_selection
from .sus import stochastic_universal_sampling
from .ts import tournament_selection

def selection(population, method):
    if method == "rws":
        return roulette_wheel_selection(population)

    elif method == "sus":
        return stochastic_universal_sampling(population)

    elif method == "ts":
        return tournament_selection(population)