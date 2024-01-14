import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

style_to_use = 'whitegrid' if 'whitegrid' in sns.style.available else sns.style.available[0]
sns.set_style(style_to_use)

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/kaggle/input/netflix-shows/netflix_titles_nov_2019.csv')
print('Done!')

df = pd.read_csv('/kaggle/input/netflix-shows/netflix_titles_nov_2019.csv')
print('Done!')

def data_inv(df):
    print('netflix movies and shows: ', df.shape[0])
    print('dataset variables: ', df.shape[1])
    print('-'*10)
    print('dateset columns: \n')
    print(df.columns)
    print('-'*10)
    print('data-type of each column: \n')
    print(df.dtypes)
    print('-'*10)
    print('missing rows in each column: \n')
    c = df.isnull().sum()
    print(c[c > 0])

data_inv(df)

dups = df.duplicated(['title', 'country', 'type', 'release_year'])
df[dups]

df = df.drop_duplicates(['title', 'country', 'type', 'release_year'])
df = df.drop('show_id', axis=1)
df['cast'] = df['cast'].replace(np.nan, 'Unknown')

def cast_counter(cast):
    if cast == 'Unknown':
        return 0
    else:
        lst = cast.split(', ')
        length = len(lst)
        return length

df['number_of_cast'] = df['cast'].apply(cast_counter)
df['cast'] = df['cast'].replace('Unknown', np.nan)

df = df.reset_index()
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

df['date_added'] = df['date_added'].fillna('January 1, {}'.format(str(df['release_year'].mode()[0])))
for i, j in zip(df['country'].values, df.index):
    if pd.isna(i):
        if ('Anime' in df.loc[j, 'listed_in']) or ('anime' in df.loc[j, 'listed_in']):
            df.loc[j, 'country'] = 'Japan'
        else:
            continue
    else:
        continue

import re

months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

date_lst = []
for i in df['date_added'].values:
    str1 = re.findall('([a-zA-Z]+)\s[0-9]+\,\s[0-9]+', i)
    str2 = re.findall('[a-zA-Z]+\s([0-9]+)\,\s[0-9]+', i)
    str3 = re.findall('[a-zA-Z]+\s[0-9]+\,\s([0-9]+)', i)
    if str1 and str2 and str3:
        date = '{}-{}-{}'.format(str3[0], months[str1[0]], str2[0])
        date_lst.append(date)

df['date_added_cleaned'] = date_lst
df = df.drop('date_added', axis=1)
df['date_added_cleaned'] = pd.to_datetime(df['date_added_cleaned'])

print(df.head())
