import pytest
import itertools as it

from euler.problem_12 import *


def test_tri():
    assert 1 == tri(1)
    assert 1 + 2 == tri(2)
    assert 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 == tri(10)


def test_tri_seq():
    assert [1, 3, 6, 10] == list(it.islice(tri_seq(), 4))


def test_divisor_count():
    assert 4 == divisor_count(6)
    assert 6 == divisor_count(28)


#@pytest.mark.skip("Working out better divisor_count")
def test_least_divisors():
    # First tri-num with more than 5 divisors is 28
    assert 28 == least_divisors(tri_seq(), 5)
