import pytest

from euler.problem_3 import factors, segmented_sieve, multiples_between


def test_factors():
    assert {2, 5} == set(factors(10))
    assert {2, 5} == set(factors(20))
    assert {3, 7} == set(factors(63))


def test_multiples_between():
    assert [4, 6] == list(multiples_between(2, 3, 7))
    # includes bounds as expected
    assert [4, 6] == list(multiples_between(2, 4, 8))


#@pytest.mark.skip(reason="working out multiples_between")
def test_segmented_sieve():
    assert [2, 3, 5, 7] == segmented_sieve(10)
    assert [2, 3, 5, 7, 11, 13] == segmented_sieve(16)
    # top-most value is excluded
    assert [2, 3, 5, 7, 11] == segmented_sieve(13)
