"""
Project Euler
Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
#from sys import argv
from functools import reduce
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def gcd(a, b):
    """Return greatest common divisor 
    using Euclid's Algorithm.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple of two numbers
    """
    return a * b // gcd(a, b)


def lcmm(numbers):
    """Return lcm of args
    Note: you can feed this a range like this:
    *range(1-10)
    """
    return reduce(lcm, numbers)


print(lcmm(numlist))
# Answer 232,792,560