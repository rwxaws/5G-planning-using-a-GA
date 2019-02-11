import numpy as np


class Cell:

    def __init__(self, xcoord, ycoord, cell_type):

        self.__xcoord = xcoord
        self.__ycoord = ycoord
        self.__cell_type = cell_type
        self.__connected_users = []
        self.__state = True
        self.__cost = self.calculate_cost()

    # getters
    def get_xcoord(self):
        return self.__xcoord

    def get_ycoord(self):
        return self.__ycoord

    def get_connected_users(self):
        return self.__connected_users

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

    def calculate_cost(self):
        if self.__cell_type == "macro":
            return 175
        elif self.__cell_type == "micro":
            return 25
        else:
            return 5

    def pprint(self):
        return """
        x = {}
        y = {}
        type = {}
        """.format(self.get_xcoord(), self.get_ycoord(), self.get_cell_type())
