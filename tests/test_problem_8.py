import pytest
import itertools as it


from euler.problem_8 import progressive, parse_num_seq, prod, max_prog_prod, PROBLEM_NUM


def test_progressive():
    expected = [[0, 1], [1, 2], [2, 3], [3, 4]]
    observed = list(progressive(it.islice(it.count(), 5), size=2))
    assert expected == observed


def test_parse_num_seq():
    assert ['1', '2', '3', '4', '5'] == list(parse_num_seq('123\n45'))
    assert ['1', '2', '3', '4', '5'] == list(parse_num_seq('12\n345'))
    assert ['1', '2', '3', '4', '5'] == list(parse_num_seq('   12\n345'))
    assert ['1', '2', '3', '4', '5'] == list(parse_num_seq('12\n345   '))


def test_prod():
    assert 120 == prod(['1', '2', '3', '4', '5'])
    assert 120 == prod(range(1, 6))


def test_provided_example():
    expected = 5832
    #observed = max(prod(x) for x in progressive(parse_num_seq(PROBLEM_NUM), 4))
    observed = max_prog_prod(parse_num_seq(PROBLEM_NUM), 4)
    assert expected == observed
