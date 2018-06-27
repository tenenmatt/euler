"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?

>>> nth_prime(10001)

"""


import itertools as it
import numpy as np
from euler.numth import sieve


def nth(seq, n):
    # Normally islice is 0-indexed, but we want 1-index for readability
    return next(it.islice(seq, n - 1, None))


def is_prime(n):
    for i in range(2, 1 + int(np.sqrt(n))):
        if (n % i) == 0:
            return False
    return True


def nth_prime(n):
    return nth((i for i in it.count(2) if is_prime(i)), n)
