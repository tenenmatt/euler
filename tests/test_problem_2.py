import pytest
import itertools as it

from euler.problem_2 import fib, is_even, sum_even_fib


def test_fib():
    expected = [1, 2, 3, 5, 8]
    # materialize first 5 values
    observed = list(it.islice(fib(), 5))
    assert expected == observed


def test_is_even():
    assert is_even(2)
    assert not is_even(5)


def test_sum_even_fib():
    assert 10 == sum_even_fib(11)
    assert 44 == sum_even_fib(35)
    # and of course we don't need a tight upper bound
    assert 44 == sum_even_fib(50)

