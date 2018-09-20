#Name: Dante Rivera
#Date: August 28th, 2018
#This program prints a user given message as a pyramid


#     1.  Prompt the user to enter a string and call it s.
#     2.  Let ls be the length of s.
#     3.  For i from 0 upto ls-1:
#     4.     Print s[0:i]
#     5.  For i from 0 upto ls-1:
#     6.     Print s[i:ls]
#     5.  Print a closing statement


str = input('Enter a word or phrase:    ')
ls = len(str)



for i in range(ls):
    print(str[0:i])
for i in range(ls):
    print(str[i:ls])


print('\n Thanks for using my program!')
