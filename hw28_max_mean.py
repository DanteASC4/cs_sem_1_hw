# Name:  Dante Rivera
# Date:  August 28th, 2018
# Takes a user given borough and displays max and mean pop over time


#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('data.csv',skiprows=5)

burrow = input('Enter a borough name:   ')
print("The largest number living in the",burrow, "is" , pop[burrow].mean())
print("The largest number living in the",burrow, "is" , pop[burrow].max())
