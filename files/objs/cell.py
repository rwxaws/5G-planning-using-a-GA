import numpy as np


class Cell:

    def __init__(self, xcoord, ycoord, cell_type):

        self.__xcoord = xcoord
        self.__ycoord = ycoord
        self.__cell_type = cell_type
        self.__connected_users = []
        self.__state = True
        self.__cost = self.__calculate_cost()
        self.__min_users = self.__calculate_min_users()
        self.__max_users = self.__calculate_max_users()

    # getters
    def get_xcoord(self):
        return self.__xcoord

    def get_ycoord(self):
        return self.__ycoord

    def get_num_connected_users(self):
        return len(self.__connected_users)

    def get_cell_type(self):
        return self.__cell_type

    def get_state(self):
        return self.__state

    def get_cost(self):
        return self.__cost

    # setters
    def set_coords(self, x, y):
        self.__xcoord = x
        self.__ycoord = y

    def set_state(self, state):
        self.__state = state

    def calculate_power(self):
        pass

    def calculate_radius(self):
        pass

    def __calculate_cost(self):
        if self.__cell_type == "macro":
            return 175
        elif self.__cell_type == "micro":
            return 25
        else:
            return 5

    def __calculate_min_users(self):
        type = self.get_cell_type()
        if type == "macro":
            return 0
        elif type == "micro":
            return 5

    def __calculate_max_users(self):
        type = self.get_cell_type()
        if type == "macro":
            return 20
        elif type == "micro":
            return 15

    def is_available(self):
        if self.get_num_connected_users() < self.__max_users:
            return True
        return False

    def pprint(self):
        return """
        x = {}
        y = {}
        type = {}
        """.format(self.get_xcoord(), self.get_ycoord(), self.get_cell_type())
