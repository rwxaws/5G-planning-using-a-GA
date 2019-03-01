import numpy as np
import copy
from ..objs.cell import Cell
from ..objs.user import User
from ..objs.plan import Plan
from ..network.net_funcs import distance, received_power


def connect_users(pool, num_macro, num_micro, num_pico=None, num_femto=None):
    """Connect users of each plan in pool to available cellular cells."""

    # iterate over every plan
    for plan in pool:
        # iterate over each user in the plan
        for user in plan.get_users():
            user.empty_close_bss()
            # loop over every cell in the plan
            for cell in plan.get_cells():
                # if user is within the radius of the cell
                if distance(user.get_xcoord(), user.get_ycoord(), cell.get_xcoord(),
                            cell.get_ycoord()) < cell.get_radius():
                    # if cell is available
                    if cell.is_available():
                        user.add_to_close_bss(cell)

            # if user is within at least one base station range
            if len(user.get_close_bss()) > 0:
                desired = user.get_close_bss()[0]
                for tested_cell in user.get_close_bss()[1:]:
                    dist1 = distance(desired.get_xcoord(),
                                     desired.get_ycoord(),
                                     user.get_xcoord(),
                                     user.get_ycoord())
                    dist2 = distance(tested_cell.get_xcoord(),
                                     tested_cell.get_ycoord(),
                                     user.get_xcoord(),
                                     user.get_ycoord())

                    num_bs = num_macro if desired.get_cell_type() == "macro" else num_micro
                    power1 = received_power(desired.get_power(),
                                            num_bs,
                                            dist1,
                                            desired.get_frequency(), 0, 0)

                    num_bs = num_macro if tested_cell.get_cell_type() == "macro" else num_micro
                    power2 = received_power(tested_cell.get_power(),
                                            num_bs,
                                            dist2,
                                            tested_cell.get_frequency(), 0, 0)

                    if power2 > power1:
                        desired = tested_cell
                user.set_connected_bs(desired)
                desired.add_user(user)


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
