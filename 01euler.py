"""
 Project Euler problems
# Number 1 - Multiples of 3 and 5 to 1000
goto www.projecteuler.net
"""
x = 999
multiples = []

while x > 0:
    if x % 5 == 0:
        multiples.append(x)
    elif x % 3 == 0:
        multiples.append(x)
    x = x - 1
print(multiples)
sum = 0
for item in multiples:
    sum = sum + item
print()
print()
print("Sum of all the multiples of 3 and 5 is: ", sum)
print()
