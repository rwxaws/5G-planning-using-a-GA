class User(object):
    """Representation of a single user in an area.

    Attributes:
        _xcoord: (int) the x coordinate of the user.
        _ycoord: (int) the y coordinate of the user.
        _close_bss: (list of) cells close by to the user.
        _connected_bs: (list of) the base station that the user is currently connected to.
        _received_power: (number) the power received from the connected bs.
        _sinr: SINR value of the user.
    """

    def __init__(self, coord_x, coord_y):
        self._coord_x = coord_x
        self._coord_y = coord_y
        self._close_bss = []
        self._connected_bs = None
        self._received_power = None
        self._sinr = None

    # getters
    def get_xcoord(self):
        return self._coord_x

    def get_ycoord(self):
        return self._coord_y

    def get_close_bss(self):
        return self._close_bss

    def get_connected_bs(self):
        return self._connected_bs

    def get_received_power(self):
        return self._received_power

    def get_sinr(self):
        return self._sinr

    # setters
    def set_connected_bs(self, bs):
        self._connected_bs = bs

    def set_received_power(self, power):
        self._received_power = power

    def set_sinr(self, sinr):
        self._sinr = sinr

    def add_to_close_bss(self, base_station):
        self._close_bss.append(base_station)

    def empty_close_bss(self):
        self._close_bss = []

    def is_connected(self):
        if self.get_connected_bs() is not None:
            return True
        return False

    def pprint(self):
        """Returns info about the user in a human readable format."""

        return """
        x            = {}
        y            = {}
        connected to = {}
        SINR         = {}
        """.format(self.get_xcoord(),
                   self.get_ycoord(),
                   self.get_connected_bs(),
                   self.get_sinr())
