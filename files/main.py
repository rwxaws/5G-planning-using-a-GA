# std library imports
import copy
import csv
import random
import os

from .helper_funcs.generators_funcs import (
    generate_candidate_points,
    generate_initial_population,
    generate_users
)

from .helper_funcs.helper import (
    find_best_plan,
    output_plans
)

from .selection.selection import selection
from .crossover.crossover import crossover
from .mutation.mutation import mutation
from .consts.constants import *


# lists
users            = []
candidate_points = []
pool             = []
best_plans       = []

# generate users
users = generate_users(NUM_USERS, AREA)

# generate candidate points (used to plant cells)
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
                                   MICRO_RADIUS,
                                   NUM_PICO,
                                   PICO_RADIUS,
                                   NUM_FEMTO,
                                   FEMTO_RADIUS)

# add the best plan from the initial population
for plan in pool:
    plan.operate()
best_plans.append(find_best_plan(pool))

# start of the genetic algorithm
for generation in range(NUM_GENERATIONS):
    print("GENERATION #{}".format(generation + 1)) 
    for plan in pool:
        plan.operate()
        print(plan.pprint())

    # selection
    pool = selection(pool, SELECTION_METHOD)

    # crossover
    cross_point = random.randint(1, len(pool) - 1)
    pool = crossover(pool, CROSSOVER_PROBABILTY, cross_point, CROSSOVER_METHOD, ALPHA)

    # mutation
    mutation(pool, AREA, MUTATION_PROBABILTY, MUTATION_METHOD) 

    # selection of the best plan from each generation
    best_plans.append(find_best_plan(pool))


# create figs directory if it doesn't exist
if "figs" not in os.listdir("files"):
    os.mkdir("files/figs")
output_plans(best_plans)
