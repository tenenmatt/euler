"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

>>> max(factors(600851475143))

"""


from euler.numth import multiples


def factors(n):
    """
    Return just the prime factors (without powers) of n

    >>> list(factors(40))
    [2, 5]

    """
    # For large n, better to use segmented_sieve, but that's still slow.
    #return (p for p in sieve(n) if n % p == 0)
    return (k for k, v in multiples(n))
