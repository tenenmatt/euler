import pytest

from euler.problem_7 import nth_prime, is_prime


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(13)
    assert not is_prime(40)


def test_provided_example():
    assert 13 == nth_prime(6)
