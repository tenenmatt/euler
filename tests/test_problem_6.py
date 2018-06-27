import pytest

from euler.problem_6 import square_diff


def test_provided_example():
    #assert 2640 == square_sum(10) - sum_squares(10)
    assert 2640 == square_diff(10)
