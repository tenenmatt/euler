import pytest

from euler.problem_4 import is_palindrome, max_palindrome_prod


def test_is_palindrome():
    assert is_palindrome(8)
    assert is_palindrome(99)
    assert is_palindrome(9009)
    assert is_palindrome(123454321)
    assert not is_palindrome(2345)


def test_max_palindrome_prod():
    assert 9009 == max_palindrome_prod(2)
