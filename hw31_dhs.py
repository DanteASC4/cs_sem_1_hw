# Name:  Dante Rivera
# Date:  August 28th, 2018
# Fraction of Children in shelters from 2013

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Prompting for df and output name
f_name = input('Enter the file name:  ')
o_name = input('Enter the output file name:  ')

# Opening df
homeless = pd.read_csv(f_name)

# Getting fraction
homeless['Fraction'] = homeless["Total Children in Shelter"] / homeless['Total Individuals in Shelter']

# Graphing data
homeless.plot(x="Date of Census", y="Fraction")

# Saving figure
fig = plt.gcf()
fig.savefig('student.png')

# Display data
plt.show()
