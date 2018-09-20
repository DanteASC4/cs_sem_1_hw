#Name: Dante Rivera
#Date: August 27th, 2018
#This program prompts the user for a message, and prints it normally, then in uppercase, then lowercase



msg = input('Enter a message: \n')


def upper_lower(string):
    print(string)
    print(string.upper())
    print(string.lower())


upper_lower(msg)
