import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Titanic.csv')
data = data.rename(columns={'Sex':'Gender'})

print(data.head(5))
print(data.dtypes)
print(data.columns.tolist())

nominal_cat = ['Name','Ticket','Cabin']

data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

print(data['Gender'].value_counts())

gender_categories = ['female', 'male']
data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print('Median gender:', median_gender)

print(data['Embarked'].value_counts())

embarked_categories = ['S', 'C', 'Q']
data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)
 
median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
sns.set_style('whitegrid')

sns.countplot(x='Survived', data=data)
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
plt.show()


sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

sns.countplot(x='Survived', data=data, hue='Survived', palette='winter', legend=False)
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')
plt.show()

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()

num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender', 'PassengerId', 'Survived'], axis=1)

num_data = num_data.fillna(num_data.median())

labels = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

for label in labels:
    plt.boxplot(num_data[label])
    plt.title('Distribution of ' + label)
    plt.show()