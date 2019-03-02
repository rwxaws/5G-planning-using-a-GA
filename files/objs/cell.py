import numpy as np


class Cell(object):
    """Representations of cellular network cells.

    Attributes:
        _xcoord: The x coordinate of the cell.
        _ycoord: The y coordinate of the cell.
        _cell_type: The type of the cell.
        _connected_users: A list of users currently connected to the cell.
        _state: The state of the cell(turned on or not).
        _cost: The cost of deploying a cell.
        _min_users: The minimum number of users that must be maintained for
                  the cell to remain active.
        _max_users: The maximum number of users that the cell can hold.
        _radius: The radius that the cell covers.
        _power: The power at which the cell is operating.
        _frequency: The frequency at which the cell is operating..
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

    def get_min_users(self):
        """Returns the minimum number of users that must be connected."""
        return self._min_users

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

    def get_power(self):
        """Returns the power(in watts) of the base station."""
        return self._power

    def get_frequency(self):
        """Returns the frequency used in the base station."""
        return self._frequency

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
        properties = {"fixed_macro": [175, 0, 20, 1000, 40, 3.5],
                      "macro": [175, 10, 20, 1000, 40, 3.5],
                      "micro": [25, 5, 10, 100, 10, 28],
                      "pico": 5,
                      "femto": 1}

        cell_type = self.get_cell_type()
        self._cost = properties[cell_type][0]
        self._min_users = properties[cell_type][1]
        self._max_users = properties[cell_type][2]
        self._radius = properties[cell_type][3]
        self._power = properties[cell_type][4]
        self._frequency = properties[cell_type][5]

    def add_user(self, user):
        """Adds the user to the list of connected users."""
        self._connected_users.append(user)

    def is_available(self):
        """Returns whether the base station is available
        for the user to connect to."""

        if self.get_num_connected_users() < self._max_users:
            return True
        return False

    def check_if_needed(self):
        """Checks if the cell is neeeded based on the number of connected users.

        if the number of connected users is less than the minimum then the cell
        is turned off and the users are left unconnected."""

        if self.get_num_connected_users() < self.get_min_users():
            self.set_state(False)

            # remove each user
            for user in self._connected_users:
                user.set_connected_bs(None)
            self._connected_users = []

    def pprint(self):
        """Returns information about cell in a human readable format."""

        return """
        x = {}
        y = {}
        type = {}
        # users = {}
        """.format(self.get_xcoord(),
                   self.get_ycoord(),
                   self.get_cell_type(),
                   self.get_num_connected_users())
