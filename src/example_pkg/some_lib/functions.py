from example_pkg.some_lib.some_submodule.more_functions import maximum


def recursive_max(some_list):
    """finds the maximum item in a list with a recursive approach
    """
    if len(some_list) == 1:
        return some_list[0]
    else:
        return maximum(some_list[0], recursive_max(some_list[1:]))
