"""
Write a function named sum_to
that accepts a single integer, n,
and returns the sum of the integers
from 1 to n.
"""


def sum_to(n: int) -> int:
    return sum(range(n + 1))


"""
Write a function named largest
that takes a list of numbers as an
argument and returns the largest
number in that list.
"""


def largest(nums: list) -> int:
    return max(nums)


"""
Write a function named occurrences
that takes two string arguments as
input and counts the number of
occurrences of the second string
inside the first string.
"""


def occurrences(str1: str, str2: str) -> int:
    pass


"""
Write a function named product that
takes an arbitrary number of numbers,
multiplies them all together, and
returns the product.
(HINT: Review your notes on *args).
"""


def product(*args: float) -> float:
    pass
