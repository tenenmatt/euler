import pytest

from euler.problem_13 import *


def test_parse_num_string():
    nums = '''
1
2
4
8
16
32
64
128
'''
    assert [1, 2, 4, 8, 16, 32, 64, 128] == parse_num_string(nums)


def test_by_place():
    nums = [12, 34, 56]
    assert [[2, 4, 6], [1, 3, 5]] == by_place(nums)
