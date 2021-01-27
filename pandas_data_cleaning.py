import pandas as pd

movies = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\movies.csv', sep=',')

tags = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\tags.csv', sep=',')

ratings = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\ratings.csv', sep=',')

print(movies.shape)
print(movies.isnull().any())
print()
print(ratings.isnull().any())
print()
print(tags.isnull().any())
print()
print(tags.shape)
print()


tags = tags.dropna()
print(tags.isnull().any())
print(tags.shape)







# http://pandas.pydata.org/pandas-docs/version/0.15.2/missing_data.html#numeric-replacement