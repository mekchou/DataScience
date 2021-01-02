import numpy as np
array_1 = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print(array_1)
print()

array_1_slice = array_1[:2,1:3]
print(array_1_slice)
# array_1_slice is referencing array_1 but has its own index
print(array_1_slice[0,0])
# to have a copy, must use np.array
array_1_slice2 = np.array(array_1[:2,1:3])
print()

# since array_1_slice is referencing array_1, change array_1_slice will change array_1 as well
array_1_slice[0,0] = 1000
print(array_1)
print(array_1_slice)
print(array_1_slice2)
print()
# using both integer indexing & slicing generates an array of lower rank
row_rank1 = array_1[1,:]
print(row_rank1,row_rank1.shape)
# slicing alone generates an array of the same rank
row_rank2 = array_1[1:2,:]
print(row_rank2,row_rank2.shape)
