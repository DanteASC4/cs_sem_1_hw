#Name: Dante Rivera
#Date: August 27th, 2018
#This program returns the ascii code for every character in a given string


#Prompting user input
str = input('Enter a word or phrase: \n')


def char_codes(string):
    for i in string:   #Looping through each char in string
        print(ord(i))  #Printing the ascii code of each char in string



char_codes(str) #Calling the function
