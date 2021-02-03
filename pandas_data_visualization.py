import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\movies.csv', sep=',')

tags = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\tags.csv', sep=',')

ratings = pd.read_csv(r'C:\Users\MekChou\OneDrive\Code\Panda\ml-25m\ratings.csv', sep=',')

# ratings.hist(column='rating', figsize=(15,10))
ratings.boxplot(column='rating',figsize=(15,20))
plt.show()
