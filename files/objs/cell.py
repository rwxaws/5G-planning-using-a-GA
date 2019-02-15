import numpy as np


class Cell(object):
    """Representations of cellular network cells.

    Attributes:
        _xcoord: The x coordinate of the cell.
        _ycoord: The y coordinate of the cell.
        _cell_tyep: The type of the cell.
        _connected_users: A list of users currently connected to the cell.
        _state: The state of the cell(turned on or not).
        _cost: The cost of deploying a cell.
        _min_users: The minimum number of users that must be maintained for
                  the cell to remain active.
        _max_users: The maximum number of users that the cell can hold.
    """

    def __init__(self, xcoord, ycoord, cell_type):

        self._xcoord = xcoord
        self._ycoord = ycoord
        self._cell_type = cell_type
        self._connected_users = []
        self._state = True
        self._cost = self._calculate_cost()
        self._min_users = self._calculate_min_users()
        self._max_users = self._calculate_max_users()

    # getters
    def get_xcoord(self):
        """Returns the x coordinate of the cell."""
        return self._xcoord

    def get_ycoord(self):
        """Returns the y coordinate of the cell."""
        return self._ycoord

    def get_num_connected_users(self):
        """Returns the number of currently connected users."""
        return len(self._connected_users)

    def get_cell_type(self):
        """Returns the cell type."""
        return self._cell_type

    def get_state(self):
        """Returns whether the base station is active or not."""
        return self._state

    def get_cost(self):
        """Returns the cost of the base station."""
        return self._cost

    # setters
    def set_coords(self, x, y):
        """Sets the coordinates of the base station."""
        self._xcoord = x
        self._ycoord = y

    def set_state(self, state):
        """Sets the state of the base station."""
        self._state = state

    def calculate_power(self):
        pass

    def calculate_radius(self):
        pass

    def _calculate_cost(self):
        """Set the cost of the base station."""

        if self._cell_type == "macro":
            return 175
        elif self._cell_type == "micro":
            return 25
        else:
            return 5

    def _calculate_min_users(self):
        """Returns the minimal number of users that the base station
            needs to be turned on."""

        type = self.get_cell_type()
        if type == "macro":
            return 0
        elif type == "micro":
            return 5

    def _calculate_max_users(self):
        """Returns the maximum number of users
        that the base station can hold."""

        type = self.get_cell_type()
        if type == "macro":
            return 20
        elif type == "micro":
            return 15

    def is_available(self):
        """Returns whether the base station is available
        for the user to connect to."""

        if self.get_num_connected_users() < self._max_users:
            return True
        return False

    def pprint(self):
        """Returns information about cell in a human readable format."""

        return """
        x = {}
        y = {}
        type = {}
        """.format(self.get_xcoord(), self.get_ycoord(), self.get_cell_type())
