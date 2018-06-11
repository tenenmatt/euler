import itertools as it
import numpy as np
import pdb


# TODO: With large values of n, sieve is pretty inefficient
# (even with segmentation). Better to just iterate over factors?


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


def factors(n):
    #return (p for p in range(2, n) if is_prime(p) and n % p == 0)
    return (p for p in sieve(n) if n % p == 0)

