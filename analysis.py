# Project 
#Agnieszka Waszczuk 

# import library pandas
import pandas as pd

# create a list with new column names
headers=['sepal_lenght_cm','sepal_width_cm','petal_lenght_cm','petal_width_cm','class']

# read csv file without the headers
iris = pd.read_csv('iris.data',header=None)

# assign new header names to dataset
iris.columns = headers

# print the table
print(iris)


print(iris.describe())
