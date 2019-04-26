import numpy as np

from ..consts.constants import AREA


def non_uniform_mutation(cell, dist):
    """Apply non uniform mutation on cell.

    Args:
        cell: The cell to apply the mutation over.
        dist: Type of distribution (cauchy or gaussian)

    Returns:
        None
    """

    if dist == "cauchy":
        dy = round(np.random.standard_cauchy(), 3)
        dx = round(np.random.standard_cauchy(), 3)
    elif dist == "gaussian":
        dx = round(np.random.normal(), 3)
        dy = round(np.random.normal(), 3)
    x_coord = cell.get_xcoord() + dx
    y_coord = cell.get_ycoord() + dy

    if x_coord > AREA or x_coord < AREA:
        x_coord = round(np.random.random() * AREA, 3)

    if y_coord > AREA or y_coord < AREA:
        y_coord = round(np.random.random() * AREA, 3)

    cell.set_coords(x_coord, y_coord)
