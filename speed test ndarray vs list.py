import numpy as np
import timeit

size = 100000
timeits = 1000

nd_array = np.arange(size)
print(nd_array)
print(type(nd_array))
# timer expects the operation as a parameter
# here we pass nd_array.sum()
timer_numpy = timeit.Timer("nd_array.sum()", "from __main__ import nd_array")
print("Time taken by numpy ndarray: %f seconds" %(timer_numpy.timeit(timeits)/timeits))

a_list = list(range(size))
# print(a_list)
print(type(a_list))
timer_list = timeit.Timer("sum(a_list)", "from __main__ import a_list")
print("Time taken by list: %f seconds" %(timer_list.timeit(timeits)/timeits))
