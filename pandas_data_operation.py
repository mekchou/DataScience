import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\movies.csv', sep=',')

tags = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\tags.csv', sep=',')

ratings = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\ratings.csv', sep=',')

# Slicing out columns
print(tags['tag'].head())
print()
print(movies[['title','genres']].head())
print()
print(ratings[1000:1010])
print()
print(ratings[-10:])
print()
tag_counts = tags['tag'].value_counts()
print()
print(tag_counts[:10])
print()
