"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


import itertools as it


def collatz_step(n):
    return n // 2 if (n % 2 == 0) else (3 * n) + 1


def collatz_seq(n):
    yield n
    while n > 1:
        n = collatz_step(n)
        yield n


def seq_len(seq):
    """
    Return the length of a sequence

    """
    return sum(1 for __ in seq)


def collatz_len(n):
    """
    Length of Collatz sequence starting with N

    """
    return seq_len(collatz_seq(n))


def max_len_upto(n):
    """
    Calculate length of longest collatz sequence upto n (inclusive)

    """
    return max(collatz_len(n) for n in range(1, n+1))


def longest_collatz_upto(n):
    return max(((n, collatz_len(n)) for n in range(1, n+1)),
               key=lambda x: x[1])


if __name__ == '__main__':
    largest_n = 1000000
    longest = longest_collatz_upto(largest_n)
    print("Longest Collatz(n) sequence for n < 1,000,000: {}".format(longest))
