# -*- coding: utf-8 -*-
"""Iris_flower_system_using_Decision Tree Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iJduICYXoNjLg-cOCy3JW4ZR5Nl14yxA

# Iris Dataset

Iris dataset is a typical machine learning classification problem. There are three species of Iris flower. When a new flower is given, we need to predict it belongs to which type.[link text](https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.lac.inpe.br%2F~rafael.santos%2FDocs%2FCAP394%2FWholeStory-Iris.html&psig=AOvVaw08URbarHxIsjjTxqsukADi&ust=1692374880058000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCMDSwPCJ5IADFQAAAAAdAAAAABAD)
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
# %pylab inline
# %matplotlib inline

import warnings
warnings.filterwarnings('ignore')

# load the iris datasets
iris = datasets.load_iris()
#df = pd.DataFrame(data.data, columns=data.feature_names)
#df.head()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
df.head()

df["target"].value_counts()

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and 'target' is the column you want to use for hue
sns.FacetGrid(df, hue="target", height=6).map(plt.scatter, "petal length (cm)", "petal width (cm)").add_legend()

plt.show()

"""### Apply on Iris Dataset"""

# fit a CART model to the data
#model = DecisionTreeClassifier()
model = DecisionTreeClassifier(criterion="entropy",max_depth=2)

model.fit(iris.data, iris.target)
print(model)

model.score(iris.data, iris.target)

"""### Make predictions"""

expected = iris.target
predicted = model.predict(iris.data)

"""### Summarize the fit of the model"""

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

"""## Tunning parameters"""

def Decision_Tree(Type,Depth):
        # import some data to play with
        iris = datasets.load_iris()
        X = iris.data[:, :2]  # we only take the first two features.
        Y = iris.target
        h = .02  # step size in the mesh
        # we create an instance of Neighbours Classifier and fit the data.
        model =DecisionTreeClassifier(criterion=Type,max_depth=Depth)

        model.fit(X, Y)
        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, m_max]x[y_min, y_max].
        x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
        y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure(1, figsize=(4, 3))
        plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.show()

        model.fit(iris.data, iris.target)
        expected = iris.target
        predicted = model.predict(iris.data)
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))

from IPython.html import widgets
from IPython.html.widgets import interact
from IPython.display import display

i = interact(Decision_Tree, Type=['gini','entropy'],Depth=(1,10))