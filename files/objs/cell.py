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
        """ returns the x coordinate of the cell """
        return self.__xcoord

    def get_ycoord(self):
        """returns the y coordinate of the cell """
        return self.__ycoord

    def get_num_connected_users(self):
        """returns the number of currently connected users """
        return len(self.__connected_users)

    def get_cell_type(self):
        """ returns the cell type
        possible cell types include {macro, micro, pico, femto}
        """
        return self.__cell_type

    def get_state(self):
        """ returns whether the basestation is active or not """
        return self.__state

    def get_cost(self):
        """ returns the cost of the base station """
        return self.__cost

    # setters
    def set_coords(self, x, y):
        """ sets the coordinates of the basestations """
        self.__xcoord = x
        self.__ycoord = y

    def set_state(self, state):
        """ sets the state of the basestation """
        self.__state = state

    def calculate_power(self):
        pass

    def calculate_radius(self):
        pass

    def __calculate_cost(self):
        """ set the cost of the base stations
        macro = 175
        micro = 25
        pico, femto = 5
        """
        if self.__cell_type == "macro":
            return 175
        elif self.__cell_type == "micro":
            return 25
        else:
            return 5

    def __calculate_min_users(self):
        """ returns the minimal number of users that the basestation needs to be turned on
        macro = 0
        micro = 5
        """
        type = self.get_cell_type()
        if type == "macro":
            return 0
        elif type == "micro":
            return 5

    def __calculate_max_users(self):
        """ returns the maximum number of users that the basestation can hold
        macro = 20
        micro = 15
        """
        type = self.get_cell_type()
        if type == "macro":
            return 20
        elif type == "micro":
            return 15

    def is_available(self):
        """ returns whether the basestation is available for the user to connect to
        """
        if self.get_num_connected_users() < self.__max_users:
            return True
        return False

    def pprint(self):
        """ returns detailed information about cell in a human readable format
        """
        return """
        x = {}
        y = {}
        type = {}
        """.format(self.get_xcoord(), self.get_ycoord(), self.get_cell_type())
