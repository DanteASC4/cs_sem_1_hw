#Name: Dante Rivera
#Date: August 30th 2018
#Display data from csv based on user input

#Import pandas for reading and analyzing CSV data:
import pandas as pd

c_f = input('Enter CSV file name: ')         #Name of the CSV file
att = input('Attribute to search by? (Plate ID, Registration State, Plate Type, etc...):    ')
tickets = pd.read_csv(c_f)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[att].value_counts()[:10]) #Print out the dataframe
