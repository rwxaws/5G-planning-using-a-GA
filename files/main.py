from .objs.cell import Cell
from .objs.user import User
from .objs.plan import Plan
from .helper_funcs.helper import generate_users, generate_candidate_points, generate_initial_population

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


# generate initial population
pool = generate_initial_population(10,
                                   candidate_points, users,
                                   NUM_MACROCELLS,
                                   DISTANCE_MACROCELLS,
                                   NUM_MICROCELLS,
                                   DISTANCE_MICROCELLS)

for plan in pool:
    plan.pprint()


users_x_positions = [user.get_xcoord() for user in users]
users_y_positions = [user.get_ycoord() for user in users]

# candidate_point_x, candidate_point_y = zip(*candidate_points)
candidate_point_x1, candidate_point_y1 = zip(*pool[0].get_candidate_points())
candidate_point_x2, candidate_point_y2 = zip(*pool[1].get_candidate_points())


f1 = plt.figure(1)
plt.grid(which="major", axis="both", linewidth=2)
plt.xticks(np.arange(0, AREA + STEP, STEP))
plt.yticks(np.arange(0, AREA + STEP, STEP))

plt.plot(users_x_positions, users_y_positions, "k.", label="users")
plt.plot(candidate_point_x1, candidate_point_y1, "ro", label="candidate points")
# plt.plot(macrocells_x_positions, macrocells_y_positions,
#          "bX", label="macro cells")
# plt.plot(microcells_x_positions, microcells_y_positions,
#          "g^", label="micro cells")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)
f1.show()

f2 = plt.figure(2)
plt.grid(which="major", axis="both", linewidth=2)
plt.xticks(np.arange(0, AREA + STEP, STEP))
plt.yticks(np.arange(0, AREA + STEP, STEP))

plt.plot(users_x_positions, users_y_positions, "k.", label="users")
plt.plot(candidate_point_x2, candidate_point_y2, "ro", label="candidate points")
# plt.plot(macrocells_x_positions, macrocells_y_positions,
#          "bX", label="macro cells")
# plt.plot(microcells_x_positions, microcells_y_positions,
#          "g^", label="micro cells")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)
f2.show()

input()