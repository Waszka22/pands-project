# Project 
# Agnieszka Waszczuk 

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

iris.head(10)

print(iris.describe())


#The first one is the number of rows and the number of columns.
iris.shape

# The column() function prints all the columns of the dataset in a list form.
iris.columns

# Checkig missing datait will display True else False.
iris.isnull()

#correlation is used to determine pairwise correlation of all the columns of the dataset
iris.corr(method='pearson')

#print (iris.info())


# # Data Visualization 
# # draw pair plot 
# tmp = iris.drop("Id", axies=1)
# g = sns.pairplot (tmp, hue= 'Species')





# # 



# # import the numpy and matplotlib.pyplot
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA, KernelPCA
# from sklearn.datasets import make_circles

# # use random.normal() method to create a list with data
# # to draw plot random samples from a normal distribution
# np.random.seed(0)
# X, y = make_circles(n_samples=400, factor=.3, noise=.05)

# # add a title for plot
# plt.figure(figsize=(10,10))
# plt.subplot(2, 2, 1, aspect='equal')
# plt.title("Original space")

# reds = y == 0
# blues = y == 1

# # add labels to axises
# plt.scatter(X[reds, 0], X[reds, 1], c="red",s=20, edgecolor='k')
# plt.scatter(X[blues, 0], X[blues, 1], c="blue",s=20, edgecolor='k')
# plt.xlabel("$x_1$")
# plt.ylabel("$x_2$")


# # # Reference: 
# # # https://towardsdatascience.com/dimension-reduction-techniques-with-python-f36ca7009e5c
# # # https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset