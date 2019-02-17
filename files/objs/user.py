class User(object):
    """Representation of a single user in an area.

    Attributes:
        _xcoord: The x coordinate of the user.
        _ycoord: The y coordinate of the user.
        _close_bss: A list of cells close to the user.
        _connected_bs: The base station that the user is currently connected to.
    """

    def __init__(self, coord_x, coord_y):
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._close_bss = None
        self._connected_bs = None

    # getters
    def get_xcoord(self):
        """Returns the user x coordinate."""
        return self._coord_x

    def get_ycoord(self):
        """Returns the user y coordinate."""
        return self._coord_y

    def get_close_bss(self):
        """Returns the list of close by base stations."""
        return self._close_bss

    def get_connected_bs(self):
        """Returns the base station that the user is currently connected to."""
        return self._connected_bs

    def pprint(self):
        """Returns info about the user in a human readable format."""

        return """
        x = {}
        y = {}
        """.format(self.get_xcoord(), self.get_ycoord())
