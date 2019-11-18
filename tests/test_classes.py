import pytest
#  from example_pkg.some_lib.some_submodule.more_functions import maximum

from example_pkg import Maxer

# Fixtures

@pytest.fixture
def maxer():
    return Maxer()


# Test Cases

def test_add_element(maxer):
    maxer.add_element(5)
    assert maxer.max == 5

