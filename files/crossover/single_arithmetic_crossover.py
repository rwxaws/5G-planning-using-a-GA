import numpy as np


def single_arithmetic_crossover(c1, c2):
    random_allele = np.random.randint(0, len(c1.get_cells("non_fixed")))

    val1 = c1.get_cells("non_fixed")[random_allele]
    val2 = c2.get_cells("non_fixed")[random_allele]

    new_val_x = round((val1.get_xcoord() + val2.get_xcoord()) / 2, 3)
    new_val_y = round((val1.get_ycoord() + val2.get_ycoord()) / 2, 3)

    c1.get_cells("non_fixed")[random_allele].set_coords(new_val_x, new_val_y)
    c2.get_cells("non_fixed")[random_allele].set_coords(new_val_x, new_val_y)
