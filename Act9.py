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