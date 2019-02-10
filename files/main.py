from .objs.cell import Cell
from .objs.user import User
from .helper_funcs.helper import generate_cells, distance, within, distance_between_cell, same_place

import matplotlib.pyplot as plt
import numpy as np


# constants
NUM_OF_USERS = int(input("Enter the number of users:"))
AREA = int(input("Enter the search area:"))
STEP = int(input("Enter step size:"))
USERS_THRESHOLD = int(input("Enter users threshold:"))
NUM_MACROCELLS = int(input("Enter macrocells number:"))
NUM_MICROCELLS = int(input("Enter microcells number:"))
DISTANCE_MACROCELLS = int(input("Enter the distance between macrocells:"))
DISTANCE_MICROCELLS = int(input("Enter the distance between microcells:"))
FREQ_MACRO = 3.5
FREQ_SMALL_CELLS = 28

# lists
users = []
candidate_points = []
macro_cells = []
micro_cells = []

# generate users
for i in range(NUM_OF_USERS):
    x = round(np.random.uniform(0, AREA))
    y = round(np.random.uniform(0, AREA))
    user = User(x, y)
    users.append(user)

# generate candidate points
for i in range(0, AREA, STEP):
    for j in range(0, AREA, STEP):
        users_num = 0
        for user in users:
            if within(i, j, STEP, user.get_xcoord(), user.get_ycoord()):
                users_num += 1

        if users_num >= USERS_THRESHOLD:
            candidate_point_x = round(np.random.uniform(i, i + STEP))
            candidate_point_y = round(np.random.uniform(j, j + STEP))
            candidate_points.append((candidate_point_x, candidate_point_y))


# generate cells
generate_cells(candidate_points, "macro", DISTANCE_MACROCELLS,
               NUM_MACROCELLS, macro_cells)
generate_cells(candidate_points, "micro", DISTANCE_MICROCELLS,
               NUM_MICROCELLS, micro_cells)

print("# of remaining candidate points:{}".format(len(candidate_points)))
same_place(candidate_points, macro_cells)
same_place(candidate_points, micro_cells)
distance_between_cell(macro_cells)
distance_between_cell(micro_cells)

users_x = [user.get_xcoord() for user in users]
users_y = [user.get_ycoord() for user in users]

candidate_point_x, candidate_point_y = zip(*candidate_points)

macrocells_x = [macrocell.get_xcoord() for macrocell in macro_cells]
macrocells_y = [macrocell.get_ycoord() for macrocell in macro_cells]
microcells_x = [microcell.get_xcoord() for microcell in micro_cells]
microcells_y = [microcell.get_ycoord() for microcell in micro_cells]

plt.grid(which="major", axis="both", linewidth=2)
plt.xticks(np.arange(0, AREA + STEP, STEP))
plt.yticks(np.arange(0, AREA + STEP, STEP))

plt.plot(users_x, users_y, "k.", label="users")
plt.plot(candidate_point_x, candidate_point_y, "ro", label="candidate points")
plt.plot(macrocells_x, macrocells_y, "bX", label="macro cells")
plt.plot(microcells_x, microcells_y, "g^", label="micro cells")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)
plt.show()
