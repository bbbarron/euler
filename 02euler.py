"""
2euler.py
Problem 2 at www.projecteuler.py
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def fibo_sum():
    max = 4000000
    sum = 0
    N2 = 0
    N1 = 0
    N = 1  # Note starting N at zero
    z = N + 1  # starting sum for n=1, z=2
    # for i in range(max):
    while N <= max:
        # print(N, z) # print the individual (number, sum pairs)
        if N % 2 == 0 and N < max:
            sum = sum + N
        N2 = N1
        N1 = N
        if N is 0:
            N = 1
        else:
            N = N1 + N2
        z = z + N

    print()
    print()
    print("Sum of the fibonacchi numbers < 4 million is", sum)


fibo_sum()
