import copy
import csv
import random

from .helper_funcs.generators_funcs import (generate_candidate_points,
                                            generate_initial_population,
                                            generate_users)
from .helper_funcs.helper import (find_best_plan, output_plans)
from .crossover.crossover import crossover
from .mutation.mutation import mutation
from .consts.constants import (AREA,
                               STEP_SIZE,
                               USERS_THRESHOLD,
                               NUM_GENERATIONS,
                               NUM_CHROMOSOMES,
                               NUM_USERS,

                               NUM_FIXED_MACRO,
                               NUM_MACRO,
                               NUM_MICRO,
                               NUM_PICO,
                               NUM_FEMTO,

                               FIXED_MACRO_RADIUS,
                               MACRO_RADIUS,
                               MICRO_RADIUS,
                               PICO_RADIUS,
                               FEMTO_RADIUS,

                               FIXED_MACRO_FREQ,
                               MACRO_FREQ,
                               SMALL_CELL_FREQ,
                               
                               CROSSOVER_PROBABILTY,
                               MUTATION_PROBABILTY,
                               CROSSOVER_METHOD,
                               MUTATION_METHOD,
                               ALPHA)


# lists
users = []
candidate_points = []
macro_cells = []
micro_cells = []
pool = []
best_plans = []

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
                                   MICRO_RADIUS,
                                   NUM_PICO,
                                   PICO_RADIUS,
                                   NUM_FEMTO,
                                   FEMTO_RADIUS)

for generation in range(NUM_GENERATIONS):
    print("GENERATION #{}".format(generation)) for plan in pool:
        plan.operate()
        print(plan.pprint())

    cross_point = random.randint(1, len(pool) - 1)
    pool = crossover(pool, CROSSOVER_PROBABILTY, cross_point, CROSSOVER_METHOD, ALPHA)
    mutation(pool, AREA, MUTATION_PROBABILTY, MUTATION_METHOD) 
    best_plans.append(find_best_plan(pool))

output_plans(best_plans)
