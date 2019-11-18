import pytest

from example_pkg import recursive_max


@pytest.mark.parametrize(
    "test_input,expected",
    [([4], 4), ([1, 2, 3, 4, 5], 5), ([-1, -2, -3, -4], -1), ([0, 0, 0, 0, 0, 0], 0),],
)
def test_recmax(test_input, expected):
    assert recursive_max(test_input) == expected


def test_recursive_max():
    assert recursive_max([1, 2, 3]) == 3
