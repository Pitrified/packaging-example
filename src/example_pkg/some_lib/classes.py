from example_pkg.some_lib.some_submodule.more_functions import maximum


class Maxer:
    """Keep track of the maximum element seen
    """

    def __init__(self):
        self.max = 0

    def add_element(self, a):
        self.max = maximum(self.max, a)
