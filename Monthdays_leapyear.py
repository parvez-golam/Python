######################################
#
######################################

JAN, FEB, MAR, APR = 1, 2, 3, 4
MAY, JUN, JUL, AUG = 5, 6, 7, 8
SEP, OCT, NOV, DEC = 9, 10, 11, 12

# determine leapyear
def is_leap (year ):
    # Return True if ' year ' is a leap year .
    divby_4 = year % 4 == 0
    divby_100 = year % 100 == 0
    divby_400 = year % 400 == 0
    return divby_4 and (not divby_100 or divby_400)


def num_days(month, year):
    # Return number of days in the specified month
    thirty_days = (month == SEP) or (month == APR) or (month == JUN) or (month == NOV)
    thirty_one_days = not thirty_days and not (month == FEB)
    if thirty_days:
        return 30
    elif thirty_one_days :
        return 31
    elif is_leap (year):
        return 29
    else :
        return 28


print(num_days(2,2000))