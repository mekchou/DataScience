import numpy as np

start = np.zeros((4,3))
print(start)
print()
# create rank 1 ndarray 
add_rows = np.array([1,0,3])
print(add_rows)
print()
# create start + add rows
y = start + add_rows
print(y)
print()
# create 4x1 ndarray to broadcast across columns
# DOUBLE [] so that the array is not 1 dimension
add_cols = np.array([[0,1,2,3]])  
# Transpose 1x4 to 4x1
add_cols = add_cols.T
print(add_cols)
print()
x = start + add_cols
print(x)
# this will just broadcast in both dimensions... as it's a 1x1
add_scalar = np.array([1])
print(start + add_scalar)
