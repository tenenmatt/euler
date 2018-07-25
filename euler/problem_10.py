"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

>>> sum_primes_upto(10)
17
>>> sum_primes_upto(2000000)
142913828922

"""

from euler.numth import sieve


def sum_primes_upto(n):
    return sum(sieve(n))
