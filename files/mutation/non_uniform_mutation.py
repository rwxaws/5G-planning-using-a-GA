import numpy as np


def non_uniform_mutation(cell, area, dist):
    """Apply non uniform mutation on cell.

    Args:
        cell: (cell obj) the cell to apply the mutation over.
        area: (int) area of interest.
        dist: (str) type of distribution.
            - cauchy
            - gaussian

    Returns:
        None
    """

    if dist == "cauchy":
        dx = round(np.random.standard_cauchy(), 3)
        dy = round(np.random.standard_cauchy(), 3)
    elif dist == "gaussian":
        dx = round(np.random.normal(), 3)
        dy = round(np.random.normal(), 3)
    x_coord = cell.get_xcoord() + dx
    y_coord = cell.get_ycoord() + dy

    if x_coord > area or x_coord < area:
        x_coord = round(np.random.random() * area, 3)

    if y_coord > area or y_coord < area:
        y_coord = round(np.random.random() * area, 3)

    cell.set_coords(x_coord, y_coord)
