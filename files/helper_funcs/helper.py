import copy
import csv

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

from ..consts.constants import (
    AREA,
    FIXED_MACRO_RADIUS,
    MACRO_RADIUS,
    MICRO_RADIUS,
    PICO_RADIUS,
    FEMTO_RADIUS
)

from ..network.net_funcs import (
    distance,
    received_power
)

from ..objs.cell import Cell
from ..objs.plan import Plan
from ..objs.user import User


def within(x, y, size, px, py):
    """Returns true if a point (px, py) is within a range (x, y, x+size, y+size)."""
    if(px >= x and px <= x + size):
        if (py >= y and py <= y + size):
            return True
    return False


def calculate_probability(population):
    """Calculate the probability of each plan in population."""
    total_sum = sum([plan.get_fitness() for plan in population])
    for plan in population:
        probability = plan.get_fitness() / total_sum
        plan.set_probability(probability)


def find_best_plan(pool):
    """Returns the best plan of a given pool."""
    
    best_plan = pool[0]
    for plan in pool:
        if plan.get_fitness() > best_plan.get_fitness():
            best_plan = plan

    return best_plan


def output_plans(best_plans):
    """Generate a figure and file of the best_plans."""
    fitness = []
    sinr = []
    connected_users = []
    active_macro = []
    active_micro = []
    active_pico = []
    active_femto = []

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
        plt.figure(figsize=(15, 15))
        plt.gca().set_xlim([0, AREA])
        plt.gca().set_ylim([0, AREA])
        # plt.axis("equal")

        for i in range(len(fmacro_x)):
            c = plt.Circle((fmacro_x[i], fmacro_y[i]),
                           radius=FIXED_MACRO_RADIUS, color="red", alpha=0.1, clip_on=True)
            plt.gcf().gca().add_artist(c)

        for i in range(len(macro_x)):
            c = plt.Circle((macro_x[i], macro_y[i]),
                           radius=MACRO_RADIUS, color="green", alpha=0.1, clip_on=True)
            plt.gcf().gca().add_artist(c)

        for i in range(len(micro_x)):
            c = plt.Circle((micro_x[i], micro_y[i]),
                           radius=MICRO_RADIUS, color="blue", alpha=0.2, clip_on=True)
            plt.gcf().gca().add_artist(c)

        for i in range(len(pico_x)):
            c = plt.Circle((pico_x[i], pico_y[i]),
                           radius=PICO_RADIUS, color="magenta", alpha=0.25, clip_on=True)
            plt.gcf().gca().add_artist(c)

        for i in range(len(femto_x)):
            c = plt.Circle((femto_x[i], femto_y[i]),
                           radius=FEMTO_RADIUS, color="cyan", alpha=0.25, clip_on=True)
            plt.gcf().gca().add_artist(c)


        plt.plot(users_x, users_y, 'k.', label="Users")
        plt.plot(fmacro_x, fmacro_y, 'ro', label="Fixed Macro")
        plt.plot(macro_x, macro_y, 'g^', label="Macro")
        plt.plot(micro_x, micro_y, 'b*', label="Micro")
        plt.plot(pico_x, pico_y, 'mo', label="Pico")
        plt.plot(femto_x, femto_y, 'cx', label="Femto")
        plt.legend(loc="upper center", bbox_to_anchor=(
            0.5, -0.05), shadow=True, ncol=3)

        plt.savefig("./files/figs/fig" +
                    str(best_plans.index(plan)) + ".png", dpi=500, format="png")

        plt.clf()
        plt.close(plt.gcf())

        fitness.append(plan.get_fitness())
        sinr.append(plan.get_sinr())
        connected_users.append(plan.get_num_of_connected_users())
        active_macro.append(len(macro_x))
        active_micro.append(len(micro_x))
        active_pico.append(len(pico_x))
        active_femto.append(len(femto_x))

    with open("./files/figs/best_plans.csv", mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=[
                                "fitness", "SINR", "connected users",
                                "active macro", "active micro", "active pico",
                                "active femto"])
        writer.writeheader()

        for i in range(len(best_plans)):
            writer.writerow({
                "fitness": fitness[i],
                "SINR": sinr[i],
                "connected users": connected_users[i],
                "active macro": active_macro[i],
                "active micro": active_micro[i],
                "active pico": active_pico[i],
                "active femto": active_femto[i]
            })
