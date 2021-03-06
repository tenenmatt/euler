import pytest

from euler.numth import segmented_sieve, \
    multiples_between, multiples


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


def test_multiples():
    assert [(2, 3), (5, 1)] == list(multiples(2 * 2 * 2 * 5))
