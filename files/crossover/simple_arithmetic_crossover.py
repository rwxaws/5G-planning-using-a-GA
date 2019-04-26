import copy

import numpy as np


def simple_arithmetic_crossover(cell1, cell2, alpha):
    c1x = alpha * cell2.get_xcoord() + (1 - alpha) * cell1.get_xcoord()
    c2x = alpha * cell1.get_xcoord() + (1 - alpha) * cell2.get_xcoord()
    c1y = alpha * cell2.get_ycoord() + (1 - alpha) * cell1.get_ycoord()
    c2y = alpha * cell1.get_ycoord() + (1 - alpha) * cell2.get_ycoord()

    cell1.set_coords(c1x, c1y)
    cell2.set_coords(c2x, c2y)
