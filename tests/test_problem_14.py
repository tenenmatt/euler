import pytest


from euler.problem_14 import *


def test_collatz_step():
    assert 40 == collatz_step(13)
    assert 20 == collatz_step(40)


def test_collatz_seq():
    assert [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] == list(collatz_seq(13))


def test_seq_len():
    assert 10 == seq_len(collatz_seq(13))
