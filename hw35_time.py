# Name:  Dante Rivera
# Date:  August 30th, 2018
# Asks for 24 hour time, and outputs evening, afternoon, or monring depending on time.




time = int(input('Enter the time (in 24 hour time):    '))



def time_check(t):
    if t < 12:
        print('Good morning')
    if t < 17:
        print('Good afternoon')
    else:
        print('Good evening')


time_check(time)
