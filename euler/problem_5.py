"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

>>> factor_product(spanning_factors(10))
2520
>>> factor_product(spanning_factors(20))
232792560

"""


from euler.numth import multiples


# A naive way to approach this would just be to search with the predicate
# that checks divisibility explicitly
def divides(m, n):
    """ m | n """
    return n % m == 0


def divides_upto(m, n):
    """
    n is divisible by 1..m

    """
    return all(divides(i, n) for i in range(1, m+1))


# This is good for m=10, but starts to get tricky for larger values of m
# (hence temporary threshold for how high to look before giving up)
def naive_spanning_factors(m, xmax=100000):
    try:
        return next(i for i in range(1, xmax) if divides_upto(m, i))
    except StopIteration:
        return None


def spanning_factors(m):
    """
    Determine the minimal product divisible by all integers 1..m

    """
    assert m >= 2
    factors = dict()
    for i in reversed(range(2, m+1)): # range(m, 2, -1)?
        for p, k in multiples(i):
            # unless we already have p as a factor with exponent _at least_ k,
            # add it to the spanning factor set
            if not (p in factors and factors[p] >= k):
                factors[p] = k
    return factors


def factor_product(factors):
    """
    Given factors as dict of (base -> expt), calculate product

    >>> factor_product({2: 2, 3: 1, 5: 1})
    60

    """
    prod = 1
    for base, expt in factors.items():
        prod *= (base ** expt)
    return prod
