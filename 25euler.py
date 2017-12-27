"""
1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time
start = time.time()
a = 1 # F2 start value
b = 0 # F1 start value
n = 1 # Number of terms in the fibonacchi sequence
l = int(input('Enter number of digits: ')) # Number of digits in the term you are looking for

while len(str(a)) != l:
    a, b = a + b, a
    n = n + 1
print (f"{a} has {l} digits, term = {n}")
print("Program completed in", time.time() - start, "seconds")
