import pytest

from euler.problem_18 import *


def test_cumulate_triangle():
    small_tri = '''
                                  3
                                 7 4
'''
    assert [[3], [10, 7]] == cumulate_triangle(parse_triangle(small_tri))
    med_tri = '''
                                  3
                                 7 4
                                2 4 6
                               8 5 9 3
'''
    expected = [[3],
                [10, 7],
                [12, 14, 13],
                [20, 19, 23, 16]]
    assert expected == cumulate_triangle(parse_triangle(med_tri))


def test_max_path_sum():
    small_tri = '''
                                  3
                                 7 4
                                2 4 6
                               8 5 9 3
'''
    assert 23 == max_path_sum(parse_triangle(small_tri))



