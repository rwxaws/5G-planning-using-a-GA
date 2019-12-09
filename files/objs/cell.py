import numpy as np

from ..consts.constants import *


class Cell(object):
    """Representations of cellular network cells.

    Attributes:
        _xcoord: (number) the x coordinate of the cell.
        _ycoord: (number) the y coordinate of the cell.
        _cell_type: (str) the type of the cell:
            - fixed_macro
            - macro
            - mirco
            - nano
            - pico
        _connected_users: (list of) users currently connected to the cell.
        _state: (boolean) the state of the cell(turned on or not).
        _cost: (int) the cost of deploying a cell.
        _min_users: (int) the minimum number of users that must be maintained for
                  the cell to remain active.
        _max_users: (int) the maximum number of users that the cell can hold.
        _radius: (number) the radius that the cell covers.
        _power: (number) the power at which the cell is operating.
        _frequency: (number) the frequency at which the cell is operating.
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
        return self._xcoord

    def get_ycoord(self):
        return self._ycoord

    def get_num_connected_users(self):
        return len(self._connected_users)

    def get_min_users(self):
        return self._min_users

    def get_cell_type(self):
        return self._cell_type

    def get_state(self):
        return self._state

    def get_cost(self):
        return self._cost

    def get_radius(self):
        return self._radius

    def get_power(self):
        return self._power

    def get_frequency(self):
        return self._frequency

    # setters
    def set_coords(self, x, y):
        self._xcoord = x
        self._ycoord = y

    def set_state(self, state):
        self._state = state

    def _set_attributes(self):
        """Set the values of attributes depending on the cell type."""
        properties = {
            "fixed_macro":
            {
                "cost": FIXED_MACRO_COST,
                "min_users": FIXED_MACRO_MIN_USERS,
                "max_users": FIXED_MACRO_MAX_USERS,
                "radius": FIXED_MACRO_RADIUS,
                "power": FIXED_MACRO_POWER,
                "frequency": FIXED_MACRO_FREQ
            },

            "macro":
            {
                "cost": MACRO_COST,
                "min_users": MACRO_MIN_USERS,
                "max_users": MACRO_MAX_USERS,
                "radius": MACRO_RADIUS,
                "power": MACRO_POWER,
                "frequency": MACRO_FREQ
            },

            "micro":
            {
                "cost": MICRO_COST,
                "min_users": MICRO_MIN_USERS,
                "max_users": MICRO_MAX_USERS,
                "radius": MICRO_RADIUS,
                "power": MICRO_POWER,
                "frequency": SMALL_CELL_FREQ
            },

            "pico":
            {
                "cost": PICO_COST,
                "min_users": PICO_MIN_USERS,
                "max_users": PICO_MAX_USERS,
                "radius": PICO_RADIUS,
                "power": PICO_POWER,
                "frequency": SMALL_CELL_FREQ
            },

            "femto":
            {
                "cost": FEMTO_COST,
                "min_users": FEMTO_MIN_USERS,
                "max_users": FEMTO_MAX_USERS,
                "radius": FEMTO_RADIUS,
                "power": FEMTO_POWER,
                "frequency": SMALL_CELL_FREQ
            }
        }

        cell_type = self.get_cell_type()
        self._cost = properties[cell_type]["cost"]
        self._min_users = properties[cell_type]["min_users"]
        self._max_users = properties[cell_type]["max_users"]
        self._radius = properties[cell_type]["radius"]
        self._power = properties[cell_type]["power"]
        self._frequency = properties[cell_type]["frequency"]

    def add_user(self, user):
        """Adds the user to the list of connected users."""
        self._connected_users.append(user)

    def is_available(self):
        """Returns whether the base station is available for the user to connect to."""

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
