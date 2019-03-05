import pytest

from euler.problem_18 import *


def test_make_tree():
    small_tree = '''
                                  3
                                 7 4
'''
    # First, just a super-trivial single node
    assert Node(3, None, None) == make_tree(parse_triangle('3'))
    # Now lets work with the tiny tree above
    expected = Node(3, Node(7, None, None), Node(4, None, None))
    assert expected == make_tree(parse_triangle(small_tree))

    med_tree = '''
                                  3
                                 7 4
                                2 4 6
                               8 5 9 3
    '''
    expected = Node(3,
                    Node(7,
                         Node(2,
                              Node(8, None, None),
                              Node(5, None, None)),
                         Node(4,
                              Node(5, None, None),
                              Node(9, None, None))),
                    Node(4,
                         Node(4,
                              Node(5, None, None),
                              Node(9, None, None)),
                         Node(6,
                              Node(9, None, None),
                              Node(3, None, None))))
    assert expected == make_tree(parse_triangle(med_tree))


@pytest.mark.skip()
def test_max_path_sum():
    small_tri = '''
                                  3
                                 7 4
                                2 4 6
                               8 5 9 3
'''
    assert 23 == max_path_sum(parse_triangle(small_tri))



