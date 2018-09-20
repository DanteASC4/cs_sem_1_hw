# CSci 127 Teaching Staff
# October 2017
# A program that uses functions to print out months.
# Modified by: Dante Rivera


def monthString(monthNum):
    if monthNum == 1:
        return "January"
    if monthNum == 2:
        return "February"
    if monthNum == 3:
        return "March"
    if monthNum == 4:
        return "April"
    if monthNum == 5:
        return "May"
    if monthNum == 6:
        return "June"
    if monthNum == 7:
        return "July"
    if monthNum == 8:
        return "August"
    if monthNum == 9:
        return "September"
    if monthNum == 10:
        return "October"
    if monthNum == 11:
        return "November"
    if monthNum == 12:
        return "December"
    else:
        print('Invalid number try again')

def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)



# Allow script to be run directly:
if __name__ == "__main__":
    main()
