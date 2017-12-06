"""
Counting Sundays
Euler Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime
import time

# First Sunday in 1901 was 6 days after the first so, 1/7/1901
start = time.time()
startday = datetime.date(1901, 1, 6)
next_sunday = startday
sum_of_sundays = 0
while next_sunday < datetime.date(2000, 12, 30):
    next_sunday = next_sunday + datetime.timedelta(days=7)
    # First Sunday in 1901 was 6 days after the first so, 1/7/1901
    if next_sunday.day == 1:
        sum_of_sundays += 1
print("The last Sunday in the series is {}, and the total is {}".format(next_sunday, sum_of_sundays))
elapsed = (time.time() - start)
print()
print()
print ("Found in %s seconds" % (elapsed))
