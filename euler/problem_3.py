import itertools as it
import numpy as np


def factors(n):
    #return (p for p in range(2, n) if is_prime(p) and n % p == 0)
    return (p for p in sieve(n) if n % p == 0)


# Who doesn't love the Sieve of Eratosthenes?
def sieve(n):
    assert n > 1
    flags = np.full(n, True, dtype=bool)
    for i in range(2, 1+int(np.sqrt(n))):
        if flags[i]:
            for j in it.takewhile(lambda x: x < n,
                                  (i**2 + m * i for m in it.count(0))):
                flags[j] = False
    return (i for i in range(2, n) if flags[i])


def segmented_sieve(n, delta=None):
    if delta is None:
        delta = int(np.sqrt(n))
    low_segment = sieve(delta) # primes in the first segment
    # now find primes for other segments
    pass
