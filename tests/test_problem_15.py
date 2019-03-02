import pytest


from euler.problem_15 import *


def test_grid_paths():
    assert 2 == grid_paths(1, 1)
    assert 4 == grid_paths(1, 3)
    assert 5 == grid_paths(4, 1)
    # Original example
    assert 6 == grid_paths(2, 2)
