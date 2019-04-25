import copy

import numpy as np

from ..network.net_funcs import distance, received_power
from ..objs.cell import Cell
from ..objs.plan import Plan
from ..objs.user import User


def print_pop(population_pool, num_macro, num_micro):
    """Print the population in a human readable format."""
    print("##########")
    print("MACRO CELLS")
    for macro_cell in population_pool[0:num_macro]:
        print(macro_cell.pprint())
    print("##########\n")

    print("##########")
    print("MICRO CELLS")
    for micro_cell in population_pool[num_macro: num_macro + num_micro]:
        print(micro_cell.pprint())
    print("##########\n")


def within(x, y, size, px, py):
    """Returns true if a point (px, py) is within a range (x, y, x+size, y+size)."""
    if(px >= x and px <= x + size):
        if (py >= y and py <= y + size):
            return True
    return False


def calculate_probability(population):

    total_sum = sum([plan.get_fitness() for plan in population])
    for plan in population:
        probability = plan.get_fitness() / total_sum
        plan.set_probability(probability)
