import copy
import csv

from .helper_funcs.generators_funcs import (generate_candidate_points,
                                            generate_initial_population,
                                            generate_users)
from .objs.cell import Cell
from .objs.plan import Plan
from .objs.user import User
from .consts.constants import (AREA,
                               STEP_SIZE,
                               USERS_THRESHOLD,

                               NUM_USERS,
                               NUM_CHROMOSOMES,
                               NUM_FIXED_MACRO,
                               NUM_MACRO,
                               NUM_MICRO,

                               FIXED_MACRO_RADIUS,
                               MACRO_RADIUS,
                               MICRO_RADIUS,

                               FIXED_MACRO_FREQ,
                               MACRO_FREQ,
                               SMALL_CELL_FREQ)

from .mutation.non_uniform_mutation import non_uniform_mutation


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
                                             STEP_SIZE,
                                             copy.deepcopy(users),
                                             USERS_THRESHOLD)


# generate initial population
pool = generate_initial_population(NUM_CHROMOSOMES,
                                   candidate_points,
                                   users,
                                   NUM_FIXED_MACRO,
                                   FIXED_MACRO_RADIUS,
                                   NUM_MACRO,
                                   MACRO_RADIUS,
                                   NUM_MICRO,
                                   MICRO_RADIUS)

for plan in pool[0:1]:
    plan.operate()
    print(plan.pprint())

for plan in pool[0:1]:
    print("Before mutation")
    print(plan.pprint())

    print("After mutation")
    non_uniform_mutation(plan, AREA)
    print(plan.pprint())


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
