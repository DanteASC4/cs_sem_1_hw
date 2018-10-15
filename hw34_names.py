# Name:  Dante Rivera
# Date:  August 30th, 2018
# Asks multiple names, last then first, and then prints them sorted




names = input('Enter comma seperated names:     ').split(';')


def name_sorter(nm):
    nm.pop()
    for i in range(len(nm)):
        print(nm[i].split(',')[1] +  nm[i].split(',')[0])





name_sorter(names)
