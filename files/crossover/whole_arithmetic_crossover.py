def whole_arithmetic_crossover(cell1, cell2, alpha):
    """Apply whole arithmetic crossover on given cells

    Args:
        cell1: (cell obj) first cell.
        cell2: (cell obj) second cell.
        alpha: (int) used in calculation of new (x, y) values.

    Returns:
        None
    """

    c1x = alpha * cell1.get_xcoord() + (1 - alpha) * cell2.get_xcoord()
    c1y = alpha * cell1.get_ycoord() + (1 - alpha) * cell2.get_ycoord()

    c2x = alpha * cell2.get_xcoord() + (1 - alpha) * cell1.get_xcoord()
    c2y = alpha * cell2.get_ycoord() + (1 - alpha) * cell1.get_ycoord()

    c1x = round(c1x, 3)
    c1y = round(c1y, 3)
    c2x = round(c2x, 3)
    c2y = round(c2y, 3)

    cell1.set_coords(c1x, c1y)
    cell2.set_coords(c2x, c2y)
