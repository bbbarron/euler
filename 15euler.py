"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import math


def test():
    n = 20
    paths = math.factorial(2 * n) / (math.factorial(n) * math.factorial(n))
    print (int(paths))


test()

# Non-programming solution:
# This is an alternate way to solve it:

# Let each movement in the horizontal direction be a zero.
# Let each movement in the vertical direction be a one.

# 1st binary# in the series of possible solutions:
# 0000000000000000000011111111111111111111
# and the last:
# 1111111111111111111100000000000000000000
# For the combinations (or solutions) in between, the amount of
#  zeros (20) should be the same as ones (20). In other
#  words, the ones and zeros have to be rearranged in all possible ways.
# This then is the same as the possible number of arranging 40 things
# in sets of 20.
# The total is: 40!/(20!)(20!)
# Just use a calculator.
# 137846528820
