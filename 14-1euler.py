# coding: utf-8
"""
Longest Collatz sequence
Euler Project – Problem 14
The following iterative sequence is defined for the set of positive integers:
n -> n / 2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence(starting at 13 and finishing at 1) contains 10
terms. Although it has not been proved yet(Collatz Problem), it is thought that
all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time

start = time.time()

startnum = 13
num = startnum
n = 1
max_num = startnum
max_n = n


def collatz(number):

    if number % 2 == 0:
        number = (number / 2)
    else:
        number = (number * 3) + 1
    return number


while (collatz(num) != 1):
    #print("Number is ", collatz(num))
    n += 1
    #print("chain length is", n)
    num = collatz(num)
print (startnum, n)
if n > max_n:
    max_n = n
    max_num = startnum
startnum += 1
n = 1
collatz(startnum)

print("Program completed in", time.time() - start, "seconds")
