"""
Calculating Pythagorean triplets using the formula
    When m and n are any two positive integers (m < n):
    a = n2 - m2
    b = 2nm
    c = n2 + m2
    Then a, b, and c form a Pythagorean Triple.
"""
m = 1
n = m + 1
for m in range(2, 100):
    a = m**2 - n**2
    b = 2 * n * m
    c = n**2 + m**2
    print("Triplet = ", a, b, c)
    print("Sum = ", a + b + c)
