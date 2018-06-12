"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

>>> max(factors(600851475143))

"""

import itertools as it
from collections import OrderedDict
import numpy as np
import pdb


# TODO: With large values of n, sieve is pretty inefficient
# (even with segmentation). Better to just iterate over factors?
# But also, worth profiling


def bool_array(n):
    """Array of bool flags, length n"""
    return np.full(n, True, dtype=bool)


# Who doesn't love the Sieve of Eratosthenes?
def sieve(n):
    """Primes p < n"""
    assert n > 1
    flags = bool_array(n)
    for i in range(2, 1+int(np.sqrt(n))):
        if flags[i]:
            for j in it.takewhile(lambda x: x < n,
                                  (i**2 + m * i for m in it.count(0))):
                flags[j] = False
    return (i for i in range(2, n) if flags[i])


def multiples_between(n, low, high):
    if n <= low <= high:
        base = np.ceil(low / n)
        return it.takewhile(lambda x: x < high,
                            (int(n * i) for i in it.count(base)))
    return []


def segmented_sieve(n, delta=None):
    if delta is None:
        delta = int(np.sqrt(n))
    # Find primes in first segment
    primes = list(sieve(delta))
    # now find primes for other segments
    seg_low, seg_high = 0, delta
    while seg_high < n:
        # Increment segment (but truncate at n)
        seg_low, seg_high = seg_high, min(n, seg_high + delta)
        seg_size = seg_high - seg_low # hence we need adaptive sizing
        # Initialize flags for this segment
        seg = bool_array(seg_size)
        # all primes up to this segment
        p_less = [p for p in primes if p < np.sqrt(seg_high)]
        for p in p_less:
            # update flags for multiples of p in [seg_low, seg_high)
            for m in multiples_between(p, seg_low, seg_high):
                seg[m - seg_low] = False
        primes.extend(i + seg_low for i in range(seg_size) if seg[i])
    return primes


def multiples(n):
    """
    Calculate all factors of a given number

    >>> list(multiples(40))
    [(2, 3), (5, 1)]

    """
    assert n > 1
    factors = OrderedDict()
    m = 2
    # Strictly speaking, this iteration is wasteful because we could skip
    # any multiples of primes. But to do that we need to _know_ which are
    # prime, which means testing individually or calculating the primes
    # up to n, which begs the question. In practice, we greedily exclude
    # composites by factoring out all their corresponding prime multiples
    # before we increment the loop.
    while m <= n:
        while n % m == 0:
            n = n / m
            factors[m] = factors.get(m, 0) + 1
        m += 1
    return (i for i in factors.items())


def factors(n):
    """
    Return just the prime factors (without powers) of n

    >>> list(factors(40))
    [2, 5]

    """
    # For large n, better to use segmented_sieve, but that's still slow.
    #return (p for p in sieve(n) if n % p == 0)
    return (k for k, v in multiples(n))
