import numpy as np
from copy import copy
from ..objs.cell import Cell


def distance(x1, y1, x2, y2):
    """ return euclidean distance """
    return round(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)


def rain(distance):
    """ returns rain attenuation in km """
    return round(9 * (distance / 1000), 3)


def fooliage(distance, frequency):
    """ returns fooliage distrubtance """
    return round(0.2 * ((frequency * 1000) ** 0.3) * ((5 / 1000) ** 0.6), 3)


def path_loss(distance, frequency, rain, fooliage):
    """ returns path loss using equation found at paper """
    return round(92.4 + 20 * np.log10(distance / 1000) + 20 * np.log10(frequency) + 0.06 * (distance / 1000) + round(np.random.uniform(0, 1), 3) + rain + fooliage, 3)


def received_power(power_bs, num_bs, distance, frequency, rain, fooliage):
    """ returns recieved power given the number of base stations using equation found at paper """
    return round((10 * np.log10(power_bs / num_bs) - path_loss(distance, frequency, rain, fooliage)) + 30, 3)


def generate_cells(candidate_points_list, type_of_cell, distance_between_cells, num_of_cells, cell_list):
    """ generate cells using the given candidate points """
    np.random.shuffle(candidate_points_list)
    temp_candidate_points_list = copy(candidate_points_list)

    # append the first cell (needed to ensure that we are not looping over an empty list)
    cell_coords = candidate_points_list.pop()
    cell = Cell(cell_coords[0], cell_coords[1], type_of_cell)
    cell_list.append(cell)

    # look for the rest
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


def within(x, y, size, px, py):
    """ returns true if a point (px, py) is within a range (x, y, x+size, y+size) """
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
