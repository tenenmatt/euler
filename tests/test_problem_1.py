import pytest


from euler.problem_1 import summed_multiples


def test_summed_multiples():
    assert 23 == summed_multiples([3, 5], 10)
