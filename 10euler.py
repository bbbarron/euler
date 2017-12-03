'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import sympy
import time

start_time = time.time()
total = 0
for n in range(2, 2000000):
    if sympy.isprime(n):
        total += n
# print(total)
# print("--- %s seconds ---" % (time.time() - start_time))
