"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""


import itertools as it
from functools import reduce

import pdb


def multiples_of(n):
    return (n * i for i in it.count(1))


def upto(seq, threshold):
    return it.takewhile(lambda x: x < threshold, seq)


# Actual problem-statement is summed_multiples([3, 5], 1000)
def summed_multiples(bases, threshold):
    mults = [set(upto(multiples_of(b), threshold))
             for b in bases]
    # sum the union of all those sets (avoid duplicates, eg multiples
    # of 15 when including 3 and 5 in bases).
    # 'reduce' here is just a terse way to take the union of all sets
    return sum(reduce(lambda x, y: x.union(y), mults))
