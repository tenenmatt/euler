"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

>>> square_diff(100)
25164150

"""


import itertools as it


def square_sum(n):
    """
    Square the sum of 1..n.

    >>> square_sum(4) == (1 + 2 + 3 + 4)^2

    """
    return sum(range(n + 1))**2


def sum_squares(n):
    return sum(i**2 for i in range(n + 1))


def square_diff(n):
    return square_sum(n) - sum_squares(n)
