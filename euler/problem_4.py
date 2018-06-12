"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.

"""


def is_palindrome(n):
    return tuple(reversed(str(n))) == tuple(str(n))


def digit_products(d):
    """
    Return iterator over all products of d-digit numbers.

    digit_products(2) = (10 * 10, 10 * 11, 10 * 12, ..., 11 * 10, ..., 99 * 99)

    """
    return (x * y
            for x in range(10**(d-1), 10**d)
            for y in range(10**(d-1), 10**d))


def max_palindrome_prod(d):
    """
    Return largest palindrome from product of all d-digit numbers.

    """
    return max(m
               for m in digit_products(d)
               if is_palindrome(m))
