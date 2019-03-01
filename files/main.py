import copy
import csv

import numpy as np

from .helper_funcs.generators_funcs import (generate_candidate_points,
                                            generate_initial_population,
                                            generate_users)
from .objs.cell import Cell
from .objs.plan import Plan
from .objs.user import User

# constants
AREA = 3000
STEP = 250
USERS_THRESHOLD = 5
NUM_USERS = 850
NUM_CHROMOSOMES = 1
NUM_MACROCELLS = 5
NUM_MICROCELLS = 10
DISTANCE_MACROCELLS = 1000
DISTANCE_MICROCELLS = 100
FREQ_MACRO = 3.5
FREQ_SMALL_CELLS = 28

# lists
users = []
candidate_points = []
macro_cells = []
micro_cells = []
pool = []

# generate users
users = generate_users(NUM_USERS, AREA)

# generate candidate points
candidate_points = generate_candidate_points(
    AREA, STEP, copy.deepcopy(users), USERS_THRESHOLD)


# generate initial population
pool = generate_initial_population(NUM_CHROMOSOMES,
                                   candidate_points, users,
                                   NUM_MACROCELLS,
                                   DISTANCE_MACROCELLS,
                                   NUM_MICROCELLS,
                                   DISTANCE_MICROCELLS)

pool[0].connect_users()
pool[0].disconnect_unneeded_cells()

with open("users_file.csv", mode="w") as users_file:
    users_file_writer = csv.writer(users_file, delimiter=",")
    users_file_writer.writerow(["pos", "coordinates", "BS type"])
    for position, users in enumerate(pool[0].get_users()):
        user_pos = position
        user_coords = (users.get_xcoord(), users.get_ycoord())
        bs_type = users.get_connected_bs().get_cell_type() if users.is_connected() else "none"

        users_file_writer.writerow([user_pos, user_coords, bs_type])
