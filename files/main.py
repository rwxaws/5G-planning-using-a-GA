from .objs.cell import Cell
from .objs.user import User
from .helper_funcs.helper import generate_cells, generate_users, generate_candidate_points

import matplotlib.pyplot as plt
import numpy as np
from copy import copy


# constants
NUM_OF_USERS = 850
AREA = 3000
STEP = 250
USERS_THRESHOLD = 5
NUM_MACROCELLS = 5
NUM_MICROCELLS = 10
DISTANCE_MACROCELLS = 1000
DISTANCE_MICROCELLS = 100
FREQ_MACRO = 3.5
FREQ_SMALL_CELLS = 28
# NUM_OF_USERS = int(input("Enter the number of users:"))
# AREA = int(input("Enter the search area:"))
# STEP = int(input("Enter step size:"))
# USERS_THRESHOLD = int(input("Enter users threshold:"))
# NUM_MACROCELLS = int(input("Enter macrocells number:"))
# NUM_MICROCELLS = int(input("Enter microcells number:"))
# DISTANCE_MACROCELLS = int(input("Enter the distance between macrocells:"))
# DISTANCE_MICROCELLS = int(input("Enter the distance between microcells:"))

# lists
users = []
candidate_points = []
macro_cells = []
micro_cells = []
pool = []

# generate users
users = generate_users(NUM_OF_USERS, AREA)

# generate candidate points
candidate_points = generate_candidate_points(
    AREA, STEP, copy(users), USERS_THRESHOLD)

# generate cells
generate_cells(candidate_points, "macro", DISTANCE_MACROCELLS,
               NUM_MACROCELLS, macro_cells)
generate_cells(candidate_points, "micro", DISTANCE_MICROCELLS,
               NUM_MICROCELLS, micro_cells)

pool = macro_cells + micro_cells

print("# of remaining candidate points:{}".format(len(candidate_points)))

users_x_positions = [user.get_xcoord() for user in users]
users_y_positions = [user.get_ycoord() for user in users]

candidate_point_x, candidate_point_y = zip(*candidate_points)

macrocells_x_positions = [macrocell.get_xcoord() for macrocell in macro_cells]
macrocells_y_positions = [macrocell.get_ycoord() for macrocell in macro_cells]
microcells_x_positions = [microcell.get_xcoord() for microcell in micro_cells]
microcells_y_positions = [microcell.get_ycoord() for microcell in micro_cells]

plt.grid(which="major", axis="both", linewidth=2)
plt.xticks(np.arange(0, AREA + STEP, STEP))
plt.yticks(np.arange(0, AREA + STEP, STEP))

plt.plot(users_x_positions, users_y_positions, "k.", label="users")
plt.plot(candidate_point_x, candidate_point_y, "ro", label="candidate points")
plt.plot(macrocells_x_positions, macrocells_y_positions,
         "bX", label="macro cells")
plt.plot(microcells_x_positions, microcells_y_positions,
         "g^", label="micro cells")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)
plt.show()
