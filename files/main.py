import copy
import csv

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
NUM_USERS = 1000
NUM_CHROMOSOMES = 50
NUM_FIXED_MACROCELLS = 5
NUM_MACROCELLS = 5
NUM_MICROCELLS = 20
DISTANCE_FIXED_MACROCELLS = 1000
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
candidate_points = generate_candidate_points(AREA,
                                             STEP,
                                             copy.deepcopy(users),
                                             USERS_THRESHOLD)


# generate initial population
pool = generate_initial_population(NUM_CHROMOSOMES,
                                   candidate_points,
                                   users,
                                   NUM_FIXED_MACROCELLS,
                                   DISTANCE_FIXED_MACROCELLS,
                                   NUM_MACROCELLS,
                                   DISTANCE_MACROCELLS,
                                   NUM_MICROCELLS,
                                   DISTANCE_MICROCELLS)

for plan in pool[0:1]:
    plan.connect_users()
    plan.disconnect_unneeded_cells()
    print(plan.calculate_connected_users())
    print(plan.calculate_cost())


with open("./files/users_file.csv", mode="w") as users_file:
    users_file_writer = csv.writer(users_file, delimiter=",")
    users_file_writer.writerow(["cell_pos",
                                "BS type",
                                "Num of connected users"])
    for position, cell in enumerate(pool[0].get_cells()):
        cell_pos = position
        bs_type = cell.get_cell_type()
        num_users = cell.get_num_connected_users()
        users_file_writer.writerow([cell_pos, bs_type, num_users])
