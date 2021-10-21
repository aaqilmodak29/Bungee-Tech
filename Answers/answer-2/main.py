import pandas as pd
import csv
df = pd.read_csv('main.csv')
df.head()
df.groupby('occupation').agg({'age': ['min', 'max']})
with open('answer1.csv', 'w') as f:
    writer = csv.writer(f)
