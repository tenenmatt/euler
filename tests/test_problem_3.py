import pytest

from euler.problem_3 import is_prime, factors


def test_factors():
    assert {2, 5} == set(factors(10))
    assert {2, 5} == set(factors(20))
    assert {3, 7} == set(factors(63))
