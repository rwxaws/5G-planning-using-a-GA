import numpy as np


def uniform_mutation(cell, area):
    """Apply uniform mutation on cell.

    Args:
        cell: (cell obj) the cell to apply the mutation on.
        area: (int) the area of interest.

    Returns:
        None
    """

    new_xcoord = round(np.random.random() * area, 3)
    new_ycoord = round(np.random.random() * area, 3)

    cell.set_coords(new_xcoord, new_ycoord)
