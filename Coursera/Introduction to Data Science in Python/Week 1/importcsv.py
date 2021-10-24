import csv

with open("C:/Users/MekChou/OneDrive/Code/Python/Coursera/Introduction to Data Science in Python/datasets/mpg.csv") as csvfile:
  mpg = list(csv.DictReader(csvfile))

print(mpg[:3])
print(mpg[0].keys())
print(sum(float(dist['cty']) for dist in mpg) / len(mpg))