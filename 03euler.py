"""
3euler.py
Project Euler problem  - Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143 ?
"""

n = int(input("Number to factor: "))


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(n)
largest_prime_factor = max(pfs)  # The largest element in the prime factor list
print()
print()
print("Prime Factors of ", n)
print("All prime factors", pfs)
print("Largest prime factor is", largest_prime_factor)
print()
print()
