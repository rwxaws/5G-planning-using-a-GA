class User:

    def __init__(self, coord_x, coord_y):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__received_power_vector = None

    def get_xcoord(self):
        return self.__coord_x

    def get_ycoord(self):
        return self.__coord_y

    def get_recieved_power_vector(self):
        return self.__received_power_vector
