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

## Description about database 

# printing data types
print (iris_data.info())
# From printing info about data we can see that there is only one categorical data and all are numerical 

# printing summary of dataset
print (iris_data.describe())

# printing summary using groupby()method
print (iris_data.groupby('class').describe())

 # printing top 10 observation
print (iris_data.head(10))

"""## 1. Outputs a summary of each variable to a single text file""
"""
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
# import matplotlib.pyplot
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
# display a histagram 
plt.show()

## Histagram of pental lenght

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=petal_len, bins='auto', color='#FFD700',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
# add a title for plot and lables
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histagram of Petal Length in cm')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

# save histogram as png
plt.savefig(f'petal_len_hist.png')
# display a histagram 
plt.show()


"""## 3.Outputs a scatter plot of each pair of variables

"""
# create scatter plot 
colors = np.arange(150)
plt.scatter(sepal_len, sepal_wid,c=colors, cmap='viridis')
plt.colorbar()
plt.title('scatter plot')
# display a scatter
plt.show()

plt.scatter(petal_len, petal_wid, cmap='viridis')
plt.title('scatter plot')
# display a scatter
plt.show()

plt.scatter(sepal_len, petal_wid, cmap='viridis')
plt.title('scatter plot')
# display a scatter
plt.show()

plt.scatter(petal_len, sepal_wid, cmap='viridis')
plt.title('scatter plot')
# display a scatter
plt.show()


"""## 4.Additional Analysis""
"""

# scatter plot 
# import the seaborn 
import seaborn as sns 
# scatter plot using kind argument/regresion
sns.pairplot (iris_data, kind='reg')
# display a plot  
plt.show()

# Pie of Irish Spicies
total_setosa = iris_data[iris_data['class'] == 'Iris-setosa'].shape[0]
total_virginica = iris_data[iris_data['class'] == 'Iris-virginica'].shape[0]
total_versicolor = iris_data[iris_data['class'] == 'Iris-versicolor'].shape[0]
#add a labels
mylabels = ["Iris-setosa", "Iris-virginica", "Iris-versicolor"]
myexplode = [0.2, 0, 0]
all_classes = np.array([total_setosa,total_virginica,total_versicolor])
plt.pie(all_classes,labels=mylabels,explode = myexplode, shadow = True)
#add title
plt.title('Pie of Irish Species')
plt.show()

Reference: 

 * https://towardsdatascience.com/
 * https://dimension-reduction-techniques-with-python-f36ca7009e5c
 * https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset
 * https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
 * https://www.pycodemates.com/2022/05/
 * iris-dataset-classification-with-python.html?utm_content=cmp-true
 * https://www.youtube.com/watch?v=02BFXhPQWHQ
 * https://www.webucator.com/article/python-color-constants-module/
 * https://pythonspot.com/matplotlib-histogram/
 * https://stackoverflow.com/questions/39841733/
 * matplotlib-histogram-how-to-display-the-count-over-the-bar
 * https://nakazakimasahito.wordpress.com/2021/01/26/
 * plotting-a-histogram-of-iris-data/
 * https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
 * https://datagy.io/seaborn-pairplot/
 * https://stackoverflow.com/questions/54317168/
 * https://python-charts.com/correlation/pairs-plot-seaborn/
 * https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-scikit-learn-iris-visualization-exercise-3.php
 * https://python-charts.com/correlation/pairs-plot-seaborn/
 * https://stackoverflow.com/questions/61673931/iris-data-regplot-out-of-dataframe-choosing-color
 * https://datagy.io/seaborn-pairplot/
 * https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/mean-median-mode/
 * https://www.educative.io/answers/what-are-head-and-tail-functions-in-pandas
 * https://www.w3schools.com/python/pandas/ref_df_info.asp#:~:text=The%20info()%20method%20prints,method%20actually%20prints%20the%20info.
 * https://www.javatpoint.com/info-function-in-python
 * https://archive.ics.uci.edu/ml/datasets/iris