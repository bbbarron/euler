"""
 Euler Project # 16
Power digit sum

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
max_number = 1000
numbers_dict = {
    n: len(word) for (n, word) in {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }.items()
}


def num_length(n):
    if n <= 20:
        return numbers_dict[n]
    elif n < 100:
        tens, rest = divmod(n, 10)
        return numbers_dict[10 * tens] + num_length(rest)
    elif n < 1000:
        hundreds, rest = divmod(n, 100)
        return num_length(hundreds) + len("hundred") + (
            len("and") + num_length(rest) if rest else 0
        )
    else:
        thousands, rest = divmod(n, 1000)
        return num_length(thousands) + len("thousand") + num_length(rest)


print(sum(num_length(n) for n in range(1, max_number + 1)))
