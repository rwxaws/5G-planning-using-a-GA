import numpy as np


def non_uniform_mutation(plan, area, dist="cauchy", probabilty=1.0):
    """Perform non uniform mutation on cells in the plan.

    Args:
        plan: Plan object.
        area: The area of interest, used to check if the cell is outside of boundaty.
        dist: Type of distribution to use(Either cauchy or gaussian).
        probabilty: Mutation probability.

    Returns:
        None
    """

    # apply only on non-fixed cells
    for cell in plan.get_cells("non_fixed"):
        random_number = np.random.random()

        if random_number <= probabilty:
            if dist == "cauchy":
                dx = np.random.standard_cauchy()
                dy = np.random.standard_cauchy()
            elif dist == "gaussian":
                dx = np.random.normal()
                dy = np.random.normal()

            cell.set_coords(cell.get_xcoord() + dx, cell.get_ycoord() + dy)
