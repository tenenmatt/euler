import pytest
from unittest import SkipTest

from euler.problem_11 import parse_numstr, parse_grid
from euler.problem_11 import subsquare, square_rows, square_cols, square_diags
from euler.problem_11 import square_products, largest_grid_product
## hor_seq, vert_seq

def test_parse_numstr():
    assert 8 == parse_numstr('08')


def test_parse_grid():
    small_grid = '''
08 02 22
49 49 99
81 49 31
'''
    assert [[8, 2, 22], [49, 49, 99], [81, 49, 31]] == parse_grid(small_grid)


def test_subsquare():
    grid = [[8, 2, 22],
            [49, 49, 99],
            [81, 49, 31]]

    # of course, the whole thing should be its own subsquare
    assert grid == subsquare(grid, 3)

    expected = [[8, 2],
                [49, 49]]
    assert expected == subsquare(grid, 2)

    expected = [[49, 99],
                [49, 31]]
    assert expected == subsquare(grid, 2, row=1, col=1)

    expected = [[2, 22],
                [49, 99]]
    assert expected == subsquare(grid, 2, row=0, col=1)

    # and we'd expect trying to access a subsquare >= 3 at some index > 0 would fail
    # (lookup catching exceptions in pytest!)


def test_square_rows():
    grid = [[8, 2, 22],
            [49, 49, 99],
            [81, 49, 31]]
    assert grid == square_rows(subsquare(grid, 3))
    # check 2 x 2
    expected = [[2, 22],
                [49, 99]]
    assert expected == square_rows(subsquare(grid, 2, row=0, col=1))


def test_square_cols():
    grid = [[8, 2, 22],
            [49, 49, 99],
            [81, 49, 31]]
    expected = [[8, 49, 81], [2, 49, 49], [22, 99, 31]]
    assert expected == square_cols(subsquare(grid, 3))
    # check 2 x 2
    expected = [[49, 49],
                [99, 31]]
    assert expected == square_cols(subsquare(grid, 2, row=1, col=1))


def test_square_diags():
    grid = [[8, 2, 22],
            [49, 49, 99],
            [81, 49, 31]]
    expected = [[8, 49, 31], [81, 49, 22]]
    assert expected == square_diags(subsquare(grid, 3))

    expected = [[2, 99], [49, 22]]
    assert expected == square_diags(subsquare(grid, 2, col=1))


def test_square_products():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    expected = {1 * 2 * 3,
                4 * 5 * 6,
                7 * 8 * 9,
                1 * 4 * 7,
                2 * 5 * 8,
                3 * 6 * 9,
                1 * 5 * 9,
                7 * 5 * 3}
    assert expected == square_products(grid)


def test_largest_grid_product():
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    expected = 72
    assert expected == largest_grid_product(grid, 2)
