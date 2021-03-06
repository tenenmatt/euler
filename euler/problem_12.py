"""
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be

1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""


# TODO: We're punting on all the interesting optimization by leveraging
# sympy for factorization. There is cleverness to be had in efficiently
# checking the factors based on primes up to sqrt(N) (see comments
# for this problem at https://projecteuler.net/overview=012)

import itertools as it
from functools import lru_cache

# It's probably cheating to lean on sympy for factorization, but
# let's start there and work backward to a native implementation.
import sympy.ntheory as nt


def tri(n):
    """
    Produce n-th triangle number.

    >>> tri(1), tri(2), tri(3), tri(10)
    1, 3, 6, 55

    """
    assert n > 0, "Expect 1-based indexes, eg tri(2) is _second_ triangle"
    # n+1 because 1-indexed inputs
    return sum(range(1, n+1))


def tri_seq():
    """
    Infinite sequence of triangle numbers

    >>> list(it.islice(tri_seq(), 4))
    [1, 3, 6, 10]

    """
    return (tri(i) for i in it.count(1))


# Just use sympy.ntheory for divisor counts (see comments above)
divisor_count = nt.divisor_count


def least_divisors(seq, m):
    """
    Produce smallest element with _strictly more than_ M divisors

    """
    return next(it.dropwhile(lambda n: divisor_count(n) <= m,
                             seq))


if __name__ == '__main__':
    ABOVE_DIVISORS = 500
    print("Smallest triangle number with over {} divisors: {}".format(
        ABOVE_DIVISORS, least_divisors(tri_seq(), ABOVE_DIVISORS)))
