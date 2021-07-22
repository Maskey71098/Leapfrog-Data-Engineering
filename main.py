#Importing the library
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Data.csv')

#Selecting specific columns 
specific_criteria = dataset[(dataset['science'] < 50) & (dataset['maths'] < 50)]

#output
print(specific_criteria)
