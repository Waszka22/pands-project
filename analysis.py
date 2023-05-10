# Project 
# Autror: Agnieszka Waszczuk 


import pandas as pd
import os
import numpy as np

iris_data = pd.read_csv('iris.data',header=None)
print(iris_data)

# rename all columns
column_names=['sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','class']
iris_data.columns = column_names
print(iris_data)

""## 1. Outputs a summary of each variable to a single text file"""git

# prepare variables
sepal_len = iris_data['sepal length in cm']
sepal_wid = iris_data['sepal width in cm']
petal_len = iris_data['petal length in cm']
petal_wid = iris_data['petal width in cm']
classes = iris_data['class']

variable_names = {'sepal_len':sepal_len,'sepal_wid':sepal_wid,'petal_wid':petal_wid,'petal_len':petal_len,'classes':classes}
for key,value in variable_names.items():
  f = open(f'{key}.txt', 'w')
  f.writelines([str(value)])
  f.close()
