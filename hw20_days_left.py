#Name: Dante Rivera
#Date: August 27th, 2018
#This program asks the user for 5 numbers, and draws using turtle and the given values




# 1.  Ask the user for the number of days until the end of the semester.
# 2.  Print out the weeks until the end of the semester (weeks = days // 7)
# 3.  Print out the leftover days (leftover = days % 7)


def leftover():
    days = int(input('Enter number of days:   '))
    weeks = days // 7
    ldays = days % 7

    print('Weeks: ', weeks)
    print('Days: ', ldays)


leftover()
