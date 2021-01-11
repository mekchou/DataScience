import numpy as np

arr = 10 * np.random.randn(2,5)
print(arr)
print(arr.mean())
# mean by row
print(arr.mean(axis = 1))
# mean by column
print(arr.mean(axis = 0))
print(arr.sum())
# sum by row
print(arr.sum(axis = 1))
# sum by column
print(arr.sum(axis = 0))
# median is under np package
print(np.median(arr, axis = 1))
print()
# create unsorted array
unsorted = np.random.randn(10)
print(unsorted)
sorted = np.array(unsorted)
# sort array
sorted.sort()
print(sorted)
print()
print(unsorted)
print()
# find unique elements
array = np.array([1,2,1,3,1,4,4,5])
print(np.unique(array))
print()
# set operations with np.array data type:
s1 = np.array(['Lexus','BMW','Toyota'])
s2 = np.array(['Lexus','Benz','Honda'])
print(s1, s2)
# exist in both array (inner join)
print(np.intersect1d(s1, s2))
# union 1d array
print(np.union1d(s1, s2))
# check in s1 that's not in s2 (left outer join)
print(np.setdiff1d(s1, s2))
# which in s1 in s2 too (boolean) (left inner join)
print(np.in1d(s1, s2))

