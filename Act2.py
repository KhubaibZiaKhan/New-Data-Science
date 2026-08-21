import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()

sns.barplot(x='day',y='total_bill',hue='sex ',data=df)
plt.title('Average Bill Per day by gender')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show()

sns.countplot(x='day',hue='sex ',data=df)
plt.title('Number of Diners per day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day',y='total_bill',data=df)
plt.title('Spread of total bil per day')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show()

sns.stripplot(x='day',y='total_bill',data=df,jitter=True)
plt.title('Every bill amount per day (strip plot)')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show()

sns.swarmplot(x='day',y='total_bill',data=df)
plt.title('Every Bill Amount Per Day(swarm plot)')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show()

sns.pointplot(x='day',y='total_bill',hue='sex ',data=df)
plt.title('Average Bill Per day by gender')
plt.xlabel('Day')
plt.ylabel('Average Bill($)')
plt.show()

sns.jointplot(x='Total Bill',y='tip',data=df)
plt.suptitle('Total Bill Vs Tip - KDE Joint Plot',y=1.02)
plt.show()

sns.pairplot(df[['Total_Bill','tip','size']])
plt.suptitle('Pair plot - Bill,Tip And party size', y=1.02)
plt.show()

sns.lmplot(x='Total Bill',y='tip',data=df)
plt.title('Total Bill Vs Tip  Trend Line')
plt.show()