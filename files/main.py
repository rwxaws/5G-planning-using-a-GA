from .objs.cell import Cell
from .objs.user import User
from .objs.plan import Plan
from .helper_funcs.generators_funcs import (generate_users,
                                            generate_candidate_points,
                                            generate_initial_population)

import numpy as np
import copy


# constants
AREA = 3000
STEP = 250
USERS_THRESHOLD = 5
NUM_USERS = 850
NUM_CHROMOSOMES = 5
NUM_MACROCELLS = 5
NUM_MICROCELLS = 10
DISTANCE_MACROCELLS = 1000
DISTANCE_MICROCELLS = 100
FREQ_MACRO = 3.5
FREQ_SMALL_CELLS = 28
# NUM_USERS = int(input("Enter the number of users:"))
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
