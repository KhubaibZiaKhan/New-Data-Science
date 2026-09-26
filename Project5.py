import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

CarsDF = pd.read_csv('bmw.csv')

CarsDF.head

CarsDF.info

CarsDF.columns

sns.pairplot(CarsDF)
plt.show()


sns.heatmap(CarsDF.corr(),annot=True)
plt.show()

sns.boxplot(data=CarsDF,x='Price_in_thousands',y='Model')
plt.show()

sns.countplot(data=CarsDF,x='Model',hue='Fuel_Type')
plt.show()