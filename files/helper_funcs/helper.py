import copy

import numpy as np
import matplotlib.pyplot as plt

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


def find_best_plan(pool):
    best_plan = pool[0]

    for plan in pool:
        if plan.get_fitness() > best_plan.get_fitness():
            best_plan = plan

    return best_plan


def output_plans(best_plans):
    for plan in best_plans:
        users_x = []
        users_y = []
        fmacro_x = []
        fmacro_y = []
        macro_x = []
        macro_y = []
        micro_x = []
        micro_y = []
        pico_x = []
        pico_y = []
        femto_x = []
        femto_y = []

        plt.clf()

        for cell in plan.get_cells('all'):
            if cell.get_cell_type() == 'fixed_macro':
                fmacro_x.append(cell.get_xcoord())
                fmacro_y.append(cell.get_ycoord())

            else:
                if cell.get_state():
                    if cell.get_cell_type() == 'macro':
                        macro_x.append(cell.get_xcoord())
                        macro_y.append(cell.get_ycoord())

                    elif cell.get_cell_type() == 'micro':
                        micro_x.append(cell.get_xcoord())
                        micro_y.append(cell.get_ycoord())

                    elif cell.get_cell_type() == 'pico':
                        pico_x.append(cell.get_xcoord())
                        pico_y.append(cell.get_ycoord())

                    elif cell.get_cell_type() == 'femto':
                        femto_x.append(cell.get_xcoord())
                        femto_y.append(cell.get_ycoord())

        for user in plan.get_users():
            users_x.append(user.get_xcoord())
            users_y.append(user.get_ycoord())

        plt.grid(True)
        plt.plot(fmacro_x, fmacro_y, 'ro')
        plt.plot(macro_x, macro_y, 'g^')
        plt.plot(micro_x, micro_y, 'b*')
        plt.plot(pico_x, pico_y, 'mo')
        plt.plot(femto_x, femto_y, 'cx')
        plt.plot(users_x, users_y, 'k.')
        plt.savefig('./files/figs/fig' +
                    str(best_plans.index(plan) + 1), dpi=500, format="png")
