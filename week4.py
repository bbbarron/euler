"""
Python Programming Essentials
Rice University
Fall 2017
Week 4, Python programming project
B.Barron
"""
import datetime


def days_in_month(year, month):
    """
    Inputs:

    year - an integer between datetime.MINYEAR and datetime.MAXYEAR representing the year

    month - an integer between 1 and 12 representing the month

    Returns:

    The number of days in the input month.
    """
    if month == 12:
        next_first = datetime.date(year + 1, 1, 1)
        # print(next_first)
    else:
        next_first = datetime.date(year, month + 1, 1)
        # print(next_first)
    dys = next_first - datetime.date(year, month, 1)
    return dys.days


def is_valid_date(year, month, day):
    """
    Inputs:

    year - an integer representing the year month

    Returns:

    True if year - month - day is a valid date and False otherwise
    """

    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return False
    elif month < 1 or month > 12:
        return False
    elif day < 1 or day > days_in_month(year, month):
        return False
    else:
        return True


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:

    year1 - an integer representing the year of the first date month1 - an integer
    representing the month of the first date day1 - an integer representing the day
    of the first date year2 - an integer representing the year of the second date
    month2 - an integer representing the month of the second date day2 - an integer
    representing the day of the second date

    Returns:
    """

    if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date2 < date1:
            return 0
        else:
            diff = date2 - date1
            return diff.days
    else:
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year - an integer representing the birthday year
      month - an integer representing the birthday month
      day - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    if not(is_valid_date(year, month, day)):
        return 0
    else:
        date2 = datetime.date.today()
        date1 = datetime.date(int(year), int(month), int(day))
        if date2 < date1:
            return 0
        else:
            age_days = date2 - date1
            return age_days.days


# REsult testing
print("You are ", age_in_days(2018, 1, 21), "days old.")  # invalid future
print("You are ", age_in_days(0, 32, 21), "days old.")   # invalid month
print("You are ", age_in_days(-4, 1, 21), "days old.")   # invalid year
print("You are ", age_in_days(0, 1, 21), "days old.")    # invalid year
print("You are ", age_in_days(2017, 10, 26), "days old.")  # valid
print("You are ", age_in_days(1951, 3, 18), "days old.")  # valid
