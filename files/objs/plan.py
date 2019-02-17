class Plan(object):
    """Representation of a single plan(cells + users)

    Attributes:
        _cell_list: List of all the cells in a given plan
        _users: List of the users associated with the plan
        _macro_cells: List of macro cells in the plan
        _micro_cells: List of micro cells in the plan(can be empty)
        _pico_cells: List of pico cells in the plan(can be empty)
        _femto_cells: List of femto cells in the plan(can be empty)
    """

    def __init__(
            self,
            cell_list,
            users,
            num_macro_cells,
            num_micro_cells=None,
            num_pico_cells=None,
            num_femto_cells=None):

        self._users = users
        self._macro_cells = cell_list[0: num_macro_cells]

        if num_micro_cells is not None:
            self._micro_cells = cell_list[num_macro_cells:
                                          num_macro_cells + num_micro_cells]
        else:
            self._micro_cells = []

        if num_pico_cells is not None:
            self._pico_cells = cell_list[num_macro_cells +
                                         num_micro_cells: num_macro_cells + num_pico_cells+num_pico_cells]
        else:
            self._pico_cells = []

        if num_femto_cells is not None:
            self._femto_cells = cell_list[num_macro_cells +
                                          num_micro_cells + num_pico_cells: num_macro_cells + num_pico_cells + num_pico_cells + num_femto_cells]
        else:
            self._femto_cells = []

    # getters
    def get_cells(self, cells_type="all"):
        """Returns a list of cells in the plan.

        Args:
            cells_type: A string of the desired cells
                      it accepts the following(all, macro, micro, pico, femto).
        """

        if cells_type == "all":
            cells = self._macro_cells + self._micro_cells + \
                self._pico_cells + self._femto_cells
        elif cells_type == "macro":
            cells = self._macro_cells
        elif cells_type == "micro":
            cells = self._micro_cells
        elif cells_type == "pico":
            cells = self._pico_cells
        elif cells_type == "femto":
            cells = self._femto_cells
        return cells

    def get_users(self):
        """Returns the list of users associated with the plan."""
        return self._users

    # setters

    def pprint(self, include_users=False):
        """Print the plan's cells and users in a human readable format.

        Args:
            include_users: A bool determining whether the users info are to be
                         printed or not.
        """

        cells = self.get_cells()
        users = self.get_users()

        print("#####")
        print("CELLS")
        print("#####")
        for cell in cells:
            print(cell.pprint())

        if include_users:
            print("#####")
            print("USERS")
            print("#####")
            for user in users:
                print(user.pprint())
