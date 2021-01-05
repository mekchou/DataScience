import numpy as np

array_1 = np.array([[11,12],[21,22],[31,32]])
print(array_1)
# print(array_1.shape)
array_1_filter = (array_1 > 15)
print(array_1_filter)
# print(array_1_filter.shape)
print(array_1[array_1_filter])
# print >20 and <30
print(array_1[(array_1 > 20) & (array_1 < 30)])
# print even number
print(array_1[(array_1 % 2 == 0)])
# add 100 to even number
array_1[array_1 % 2 == 0] += 100
print(array_1)