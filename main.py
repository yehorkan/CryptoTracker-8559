```python
# Python code for basic data processing

import pandas as pd
import numpy as np

# Creating a simple dataframe
data = {
    'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
    'Age': [20, 21, 19, 20, 19],
    'Score': [85, 80, 90, 85, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# Counting the duplicate rows
print("\nCount of duplicate rows")
print(df.duplicated().sum())

# Removing duplicates
df = df.drop_duplicates()

print("\nDataFrame after removing duplicates")
print(df)

# Finding maximum and minimum age
max_age = df['Age'].max()
min_age = df['Age'].min()

print("\nMaximum age: ", max_age)
print("Minimum age: ", min_age)

# Finding mean score
mean_score = df['Score'].mean()
print("\nMean Score: ", mean_score)

# Grouping by name
grouped = df.groupby('Name')

print("\nGrouped DataFrame:")
for name, group in grouped:
    print("\nGroup:")
    print(group)

# Apply function to calculate range (max - min)
def calculate_range(series):
    return series.max() - series.min()

age_range = df['Age'].apply(calculate_range)
score_range = df['Score'].apply(calculate_range)

print("\nAge Range: ", age_range)
print("Score Range: ", score_range)

# Creating a new column 'Performance' based on score
conditions = [
    (df['Score'] >= 85),
    (df['Score'] < 85)
]

values = ['Good', 'Average']

df['Performance'] = np.select(conditions, values)

print("\nDataFrame after adding new column 'Performance'")
print(df)

# Sorting by age and score
df = df.sort_values(['Age', 'Score'])

print("\nDataFrame after sorting by 'Age' and 'Score'")
print(df)

# Saving to csv
df.to_csv('processed_data.csv', index=False)

print("\nData saved to 'processed_data.csv'")
```
Цей код виконує основні операції обробки даних, такі як видалення дублікатів, знаходження максимального та мінімального значень, обчислення середнього значення, групування по конкретній колонці, застосування функцій до серій, додавання нових колонок, сортування та збереження даних у csv файл.