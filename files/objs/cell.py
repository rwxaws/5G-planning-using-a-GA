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
        _radius: The radius that the cell covers.
    """

    def __init__(self, xcoord, ycoord, cell_type):

        self._xcoord = xcoord
        self._ycoord = ycoord
        self._cell_type = cell_type
        self._connected_users = []
        self._state = True

        self._set_attributes()

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

    def get_radius(self):
        """Returns the radius that a cell covers."""
        return self._radius

    # setters
    def set_coords(self, x, y):
        """Sets the coordinates of the base station."""
        self._xcoord = x
        self._ycoord = y

    def set_state(self, state):
        """Sets the state of the base station."""
        self._state = state

    def _set_attributes(self):
        """Set the values of attributes depending on the cell type."""
        cell_type = self.get_cell_type()
        if cell_type == "macro":
            self._cost = 175
            self._min_users = 0
            self._max_users = 20
            self._radius = 1000
            self._power = 40

        elif cell_type == "micro":
            self._cost = 25
            self._min_users = 5
            self._max_users = 15
            self._radius = 100
            self._power = 10

        else:
            pass  # for pico + femto

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
