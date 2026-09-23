import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(base_dir, 'IMDB-Dataset.csv'))

print(data.head())
print(data.isnull().sum())

data['review'] = data['review'].str.replace(r'<br\s*/?>', ' ', regex=True)
data['word_count'] = data['review'].str.split().str.len()

data['sentiment'].value_counts().plot(kind='bar', edgecolor='black', color=['g', 'r'])
plt.ylabel("Count of reviews")
plt.xlabel("Sentiment")
plt.title("Sentiment Distribution")
plt.xticks(rotation=0)
plt.show()

plt.hist(data['word_count'])
plt.ylabel("Count of reviews")
plt.xlabel("Words per review")
plt.title("Ditribution of review Length")
plt.show()
bins_len = np.arange(0, 1050, 50)
plt.hist(data['word_count'].clip(upper=1000), edgecolor="black", bins=bins_len, color='g')
plt.ylabel("Count of reviews")
plt.xlabel("Worde per review (capped at 1000)")
plt.title("Review Length Distribution")
plt.show()
for label, color in [('positive', 'g'), ('negative', 'r')]:
    subset = data.loc[data['sentiment'] == label, 'word_count'].clip(upper=1000)
    plt.hist(subset, bins=bins_len, alpha=0.5, color=color, label=label)
plt.legend()
plt.xlabel("Words per review")
plt.ylabel("Count of reviews")
plt.title("Review Length by Sentiment")
plt.show()