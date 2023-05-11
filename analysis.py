# Project 
# Autror: Agnieszka Waszczuk 


import pandas as pd
import os
import numpy as np

iris_data = pd.read_csv('iris.data',header=None)
print(iris_data)

# name all columns
column_names=['sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','class']
iris_data.columns = column_names
print(iris_data)

## Description about database ##git 

# printing data types
print (iris_data.info())
# From printing info about data we can see that there is only one categorical data and all are numerical 

# printing summary of dataset
print (iris_data.describe())

""## 1. Outputs a summary of each variable to a single text file""

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

"""## 2. Saves a histogram of each variable to png files

"""
import matplotlib.pyplot as plt

# Data Visualisation
## Histagram for Sepal Legth (cm)
# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=sepal_len, bins='auto', color='#BF3EFF',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
# add a lable for plot
plt.xlabel('Value')
plt.ylabel('Frequency')
# add a title for plot
plt.title('Histagram of Sepal Length in cm')
# add a text for plot
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

# save histogram as png
plt.savefig(f'sepal_len_hist.png')
plt.show()

## Histagram of sepal width

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=sepal_wid, bins='auto', color='#66CD00', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
# add a lable for plot
plt.xlabel('Value')
plt.ylabel('Frequency')
# add a title for plot
plt.title('Histagram of Sepal Width in cm')
# add a text for plot
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

# save histogram as png
plt.savefig(f'sepal_wid_hist.png')

plt.show()


##Histagram petal width (cm)

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=petal_wid, bins='auto', color='#98F5FF',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
# add a lable for plot
plt.xlabel('Value')
plt.ylabel('Frequency')
# add a title for plot
plt.title('Histagram of Petal Width in cm')
# add a text for plot
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.git
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

# save histogram as png
plt.savefig(f'petal_wid_hist.png')
plt.show()

## Histagram of pental lenght

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=petal_len, bins='auto', color='#FFD700',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
# add a title for plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histagram of Petal Length in cm')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

# save histogram as png
plt.savefig(f'petal_len_hist.png')

plt.show()


"""## 2.Outputs a scatter plot of each pair of variables

"""
#adding colors 
colors = np.arange(150)
plt.scatter(sepal_len, sepal_wid,c=colors, cmap='viridis')
plt.title('Scatter plot of Sepal Lenghts v Sepal Width')
plt.colorbar()
plt.show()


plt.scatter(petal_len, petal_wid,cmap='viridis')
plt.title('Scatter plot of Pental Length v Pental Width')
plt.show()


plt.scatter(sepal_len, petal_wid, cmap='viridis')
plt.title('Scatter plot of Sepal Lenghts v Pental Width')
plt.show()


plt.scatter(petal_len, sepal_wid, cmap='viridis')
plt.title('Scatter plot of Sepal Lenghts v Sepal Width')
plt.show()

