"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product _abc_.

>>> [edge_product(a, b, c) for a, b, c in triples_with_sum(1000)]
[31875000]

Problem notes:

Brute force on all (a, b, c) < 1000 is too slow. Need to reduce search-space.

One way is to force an order (3-4-5 and 4-3-5 triangles are actually the same,
so we can assume an explicit order on tuplets).

Another potential mechanism: for (a, b, c) pythagorean triplet, so is (ma, mb, mc). So when searching for pythogorean triples, we need only consider the relatively-prime values of a, b (c follows).

Then also, c is completely determined by a, b so we should be able to restrict
ourselves to a search space on a, b rather than including c explicitly in the
results. a**2 + b**2 is a perfect square (newton's method?), a + b + sqrt(a**2 + b**2) = 1000

"""

import math


# XXX: We don't actually use this except to demonstrate the badness of the
# brute-force approach
def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2


# Naive: [(a,b,c) for a, b, c in tuples_upto(N) if is_pythagorean(a, b, c)]
# (but that's ~1s for N = 100)


def sum_edge_lengths(a, b):
    return a + b + math.sqrt(a**2 + b**2)


def pairs_upto(n):
    """
    Generate all ordered pairs (a, b) where a <= b < n

    """
    return ((a, b)
            for a in range(1, n)
            for b in range(1, n)
            if a <= b)


def hypot(a, b):
    """Calculate length of hypoteneuse of triangle with sides a, b"""
    return math.sqrt(a**2 + b**2)


def is_perfect(n):
    # Cribbed from https://stackoverflow.com/questions/15390807/integer-square-root-in-python#15391420
    def newton(n):
        """Largest x for which x**2 <= n"""
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x
    m = newton(n)
    # Perfect square when square of that integer exactly equals n
    return m * m == n


def triples_with_sum(n):
    sum_squares = lambda a, b: a**2 + b**2
    cand = [sides for sides in pairs_upto(n)
            if sum_edge_lengths(*sides) == n
            and is_perfect(sum_squares(*sides))]
    return [(a, b, int(hypot(a, b))) for a, b in cand]


def edge_product(a, b, c):
    return a * b * c

