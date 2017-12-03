"""
Sum square difference
Project Euler - Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# Try recursion routine and sum the squares
# Squared sum of the first 100 digits)
sum1 = 0
for n in range(101):
    sum1 = sum1 + n**2
print ("Sum of the squares:", sum1)  # sum of the squares

sum2 = 0
for n in range(101):
    sum2 = sum2 + n
sumsqr = sum2**2
print("Sum of the numbers, squared:", sumsqr)
print ("Difference:", (sumsqr - sum1))
