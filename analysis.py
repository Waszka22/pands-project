# Project 
# Autror: Agnieszka Waszczuk 


import pandas as pd
import os
import numpy as np

iris_data = pd.read_csv('iris.data',header=None)
print(iris_data)

column_names=['sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','class']
iris_data.columns = column_names
print(iris_data)

