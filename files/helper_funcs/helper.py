import numpy as np
from copy import copy
from ..objs.cell import Cell
from ..objs.user import User

def distance(x1, y1, x2, y2):
    """Returns euclidean distance between 2 points."""
    return round(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)


def rain_attenuation(distance):
    """Returns rain attenuation in km."""
    return round(9 * (distance / 1000), 3)


def fooliage(distance, frequency):
    """Returns fooliage ghosting."""
    return round(0.2 * ((frequency * 1000) ** 0.3) * ((5 / 1000) ** 0.6), 3)


def path_loss(distance, frequency, rain, fooliage):
    """Returns path loss using equation found at paper."""
    return round(92.4 + 20 * np.log10(distance / 1000) +
                 20 * np.log10(frequency) + 0.06 * (distance / 1000) +
                 round(np.random.uniform(0, 1), 3) + rain + fooliage, 3)


def received_power(power_bs, num_bs, distance, frequency, rain, fooliage):
    """Returns recieved power given the number of base stations.

    Args:
        power_bs: power of the base station.
        num_bs: num of base stations.
        frequency: the frequency at which the base station(s) operate.
        rain: rain attenuation.
        fooliage: foliage ghosting.

    Returns:
        A float rounded to three decimal places.
    """

    return round((10 * np.log10(power_bs / num_bs) - path_loss(distance, frequency, rain, fooliage)) + 30, 3)


def generate_cells(candidate_points_list, type_of_cell, distance_between_cells, num_of_cells, cell_list):
    """Generates cells using the given candidate points.

    Generates required cells that can be used to create a population.

    Args:
        candidate_points_list: the list of candidate points each as a tuple
        type_of_cell: a string representing the type of cell(eg: macro)
                    that is to be generated.
        distance_between_cells: the distance (in meters) between every cell.
        num_of_cells: how many cells to be generated.
        cell_list: an empty list pointer to fill with generated cells.
    """
    np.random.shuffle(candidate_points_list)
    temp_candidate_points_list = copy(candidate_points_list)

    # append the first cell (needed to ensure that we are not looping over an empty list)
    cell_coords = candidate_points_list.pop()
    cell = Cell(cell_coords[0], cell_coords[1], type_of_cell)
    cell_list.append(cell)

    # look for the remainding candidate points
    for cp in temp_candidate_points_list:
        is_well_positioned = True
        for c in cell_list:
            if distance(cp[0], c.get_xcoord(), cp[1], c.get_ycoord()) < distance_between_cells:
                is_well_positioned = False
                break

        if is_well_positioned:
            cell = Cell(cp[0], cp[1], type_of_cell)
            cell_list.append(cell)
            candidate_points_list.pop(candidate_points_list.index(cp))

        if len(cell_list) >= num_of_cells:
            break

def generate_users(num_of_users, area):
    """Generate users in a uniform random way."""
    users = []
    for _ in range(num_of_users):
        x = round(np.random.uniform(0, area))
        y = round(np.random.uniform(0, area))
        user = User(x, y)
        users.append(user)
    return users

def generate_candidate_points(area, step, users_list, users_threshold):
    """Generate candidate points in a uniform random way."""
    candidate_points = []
    for i in range(0, area, step):
        for j in range(0, area, step):
            users_num = 0
            for user in users_list:
                if within(i, j, step, user.get_xcoord(), user.get_ycoord()):
                    users_num += 1

            if users_num >= users_threshold:
                candidate_point_x = round(np.random.uniform(i, i + step))
                candidate_point_y = round(np.random.uniform(j, j + step))
                candidate_points.append((candidate_point_x, candidate_point_y))
    return candidate_points




def print_pop(population_pool, num_macro, num_micro):
    """Print the population in a human readable format."""
    print("##########")
    print("MACRO CELLS")
    for macro_cell in population_pool[0:num_macro]:
        print(macro_cell.pprint())
    print("##########\n")

    print("##########")
    print("MICRO CELLS")
    for micro_cell in population_pool[num_macro: num_macro + num_micro]:
        print(micro_cell.pprint())
    print("##########\n")


def within(x, y, size, px, py):
    """Returns true if a point (px, py) is within a range (x, y, x+size, y+size)."""
    if(px >= x and px <= x + size):
        if (py >= y and py <= y + size):
            return True
    return False


def distance_between_cell(cell_list):
    # TODO: Implement(remove get_coords)
    pass
    # for cell in cell_list:
    #     for other in cell_list:
    #         pass
    #         print("Distance = {} cell {} and cell {}, coords = ({}) ({})".format(distance(cell.get_coords()[0], other.get_coords()[0], cell.get_coords()[1], other.get_coords()[1]), cell_list.index(cell), cell_list.index(other), cell.get_coords(), other.get_coords()))


def same_place(cpl, cl):
    pass
    # for cp in cpl:
    #     for c in cl:
    #         if (cp[0] == c.get_xcoord()) and (cp[1] == c.get_ycoord()):
    #             print("Same Place")
