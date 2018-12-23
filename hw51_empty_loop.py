#Name: Dante Rivera
#Date: November 2018
#Prompts for string if empty string entered

str = input('Enter a string')

while str == '':
	print('Enter a non-empty string')
	str = input('Enter a string')
	print('That was empty, try again')