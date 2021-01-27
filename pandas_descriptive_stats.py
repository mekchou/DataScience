import pandas as pd

movies = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\movies.csv', sep=',')

tags = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\tags.csv', sep=',')

ratings = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\ratings.csv', sep=',')


# describe() shows summary statistics of dataframe
print(ratings['rating'].describe())
print()
# corr() computes pairwise Pearson coefficient of columns
print(ratings.corr())
# func = min, max, mode, median
# print(ratings['rating'].func())
# frequently used optional parameter: axis = 0 (rows) or 1 (columns)
print(ratings.mean())
print()
print(ratings['rating'].min())
print(ratings['rating'].max())
print(ratings['rating'].mode())
print(ratings['rating'].median())
print(ratings['rating'].mean(axis = 0))
print(ratings['rating'].std())
print()
# any() returns whether any element is true
# can detect if a cell matches a condition very quickly
# all() returns whether all element is true
# can detect if a column or row matches a condition very quickly

filter_1 = ratings['rating'] > 5
print(filter_1.any())
print()
print(filter_1)
print()
filter_2 = ratings['rating'] > 0
print(filter_2.all())
print()

# Some other functions: Count, Clip, Rank, Round...
# http://pandas.pydata.org/pandas-docs/stable/api.html#api-dataframe-stats