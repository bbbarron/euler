# coding: utf-8
"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
start = time.time()
num = 6


def divisors(num, divs=[], sumdiv=0):
    for x in range(1, num + 1):
        if (num % x) == 0:
            divs.append(x)
    for item in divs:
        sumdiv = sumdiv + item
    return num, sumdiv


print("Number, Divisors, Sum", num, divisors(num))

elapsed = (time.time() - start)
# print ("found %s at length %s in %s seconds" % (max[1], max[0], elapsed))
