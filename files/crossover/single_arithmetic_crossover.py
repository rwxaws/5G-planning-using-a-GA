import numpy as np


def single_arithmetic_crossover(c1, c2, alpha):
    random_allele = np.random.randint(0, len(c1.get_cells("non_fixed")))

    val1 = c1.get_cells("non_fixed")[random_allele]
    val2 = c2.get_cells("non_fixed")[random_allele]

    new_val_x1 = round((alpha * val2.get_xcoord() +
                        (1 - alpha) * val1.get_xcoord()), 3)
    new_val_y1 = round((alpha * val2.get_ycoord() +
                        (1 - alpha) * val1.get_ycoord()), 3)

    new_val_x2 = round((alpha * val1.get_xcoord() +
                        (1 - alpha) * val2.get_xcoord()), 3)
    new_val_y2 = round((alpha * val1.get_ycoord() +
                        (1 - alpha) * val2.get_ycoord()), 3)

    c1.get_cells("non_fixed")[random_allele].set_coords(new_val_x1, new_val_y1)
    c2.get_cells("non_fixed")[random_allele].set_coords(new_val_x2, new_val_y2)
