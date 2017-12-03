"""
4euler.py
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# largest possible number to use is 999
# therefore largest possible 3 digit product (start) is: (999**2)(998,001)
# smallest possible 2 digit product(end) is (100**2) (10,000)
# so, try factoring all palindromes between those endpoints

# 1) Find reverse of string - start with largest?
# 2) Check if reverse and original are same or not.
# 3) then select largest non-prime palindrome
start = 998001
end = 10000


def reverse(s):
    return s[::-1]


def isPalindrome(string):
    # Calling reverse function
    rev = reverse(s)
    # Checking if both string are equal or not
    if (s == rev):
        return True
    else:
        return False


# Main program
n = start
while n > end:
    s = str(n)
    if isPalindrome(s):
        for c in range(999, 100, -1):
            if (int(s) % c) == 0 and (int(s) / c) < 999:
                print()
                print()
                print("Palindrome", "Factor 1", "Factor 2")
                print (int(s), c, int(int(s) / c))
                print()
                print()
                exit()  # stop after first and largest instance found
    n -= 1
