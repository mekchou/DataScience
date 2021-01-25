# read_csv-> Input: .csv; Output: pandas dataframe
# read_json-> Input: .json; Output: pandas dataframe
# read_html-> Input: .html; Output: list of pandas dataframes
# read_sql_query-> Input1: .sql; Input2: Database connection; Output: pandas dataframe
# read_sql_table-> Input1: Name of SQL table in database; Input2: Database connection; Output: pandas dataframe of the table

# script: ls = list files under directory
# script: cat = display content of file

import pandas as pd
# load csv file
movies = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\movies.csv', sep=',')
print(type(movies))
print()
# show top 15. Remove 15 then show all
print(movies.head(15))
print()

# timestanps represent seconds since midnight coordicated universal time
tags = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\tags.csv', sep=',')
print(tags.head())
print()

ratings = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\ratings.csv', sep=',')
print(ratings.head())
print()

# for current analysis, we will remove timestamp
del ratings['timestamp']
del tags['timestamp']

# Data Structures
# Series

# Extract 0th row: notice that it is infact a Series
row_0 = tags.iloc[0]
print(type(row_0))
print()
print(row_0)
print()
print(row_0.index)
print()
print(row_0['userId'])
print()
print('rating' in row_0)
print()

# Data Frames
print(tags.head())
print()
print(tags.index)
print(tags.columns)
print()

# Extract row 0,11,2000 from data frames
print(tags.iloc[[0,11,2000]])
