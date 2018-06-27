import pytest

from euler.problem_5 import factor_product, spanning_factors


def test_factor_product():
    assert 2 * 2 * 3 * 5 == factor_product({2: 2, 3: 1, 5: 1})


def test_provided_example():
    assert 2520 == factor_product(spanning_factors(10))


def test_problem_statement():
    assert 232792560 == factor_product(spanning_factors(20))
