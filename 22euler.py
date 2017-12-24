"""
Euler Project – Problem 22
Names scores
Using "p022_names.txt" a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time
import csv
import string

start = time.time()

# TODO
# Read the CSV file and sort the list
# position = index + 1
# create dictionary or tuple for alphabet
# for name in name_list calculate name score
# multiply name score by position and add to total
# add name score to the total score
# print

with open('p022_names.txt', 'r') as f:
    reader = csv.reader(f)
    nmslist = list(reader)
    # Why do I get a list of lists here?
nmslist[0].sort()
names_list = nmslist[0]
print(names_list)

alphabet_number_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
# print(alphabet_number_dict)
total = 0
for name in names_list:
    nmtotal = 0
    for letter in name:
        nmtotal += alphabet_number_dict[letter]
        total += (nmtotal * (names_list.index(name)))
    print("Grand Total is: ", total)

print("Program completed in", time.time() - start, "seconds")

"""
f = open("p022_names.txt", 'r')
char_num_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
names = sorted(f.read().replace('"', '').split(','), key=str)
sum = 0
for ind, val in enumerate(names):
    temp = 0
    for x in val:
        temp += char_num_dict[x]
    sum += temp * (ind + 1)

print (sum)
"""
