class User:

    def __init__(self, coord_x, coord_y):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__close_bss = None
        self.__connected_bs = None

    # getters
    def get_xcoord(self):
        """ returns the user x coordinate """
        return self.__coord_x

    def get_ycoord(self):
        """ returns the user y coordinate """
        return self.__coord_y

    def get_close_bss(self):
        """ returns the list of close by basestations """
        return self.__close_bss

    def get_connected_bs(self):
        """ returns the basestation that the user is currently connected to """
        return self.__connected_bs