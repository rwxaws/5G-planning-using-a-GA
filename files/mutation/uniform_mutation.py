import numpy as np


def uniform_mutation(plan, area, probabilty=1.0):
    """Perform uniform mutation.

    Args:
        plan: Plan object.
        area: The area of interest, used to generate new values for coordinates.
        probabilty: Mutation probabilty.

    Returns:
        None
    """

    # apply mutation on non-fixed cells only
    for cell in plan.get_cells("non_fixed"):
        random_number = np.random.random()

        if random_number <= probabilty:
            new_xcoord = round(np.random.rand() * area, 3)
            new_ycoord = round(np.random.rand() * area, 3)
            cell.set_coords(new_xcoord, new_ycoord)
