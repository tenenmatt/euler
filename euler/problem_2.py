"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.

"""

import pdb
import itertools as it


def fib():
    """
    Produce the (infinite) Fibonacci sequence, starting 1, 2, 3, 5, ...
    
    (Note, for problem-statement we're skipping the historical "first" 1)
    
    """
    last_two = (0, 1)
    while True:
        current = sum(last_two)
        yield current
        prev_prev, prev = last_two
        last_two = (prev, current)


def is_even(x):
    return (x % 2) == 0


def sum_even_fib(upto=4e6):
    bounded_fib = it.takewhile(lambda x: x < upto, fib())
    return sum(x for x in bounded_fib if is_even(x))