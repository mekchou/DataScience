import numpy as np
array_1 = np.array([1,11,111])
print(type(array_1))
print(array_1)
print(array_1.shape)
print(array_1[0],array_1[1],array_1[2])
array_1[0]= 9
print(array_1)

array_2 = np.array([[1,11,111],[2,4,6]])
print(type(array_2))
print(array_2)
print(array_2.shape)
print(array_2[0,0],array_2[1,1],array_2[1,2])
array_2[0,0]= 9
print(array_2)

array_3 = np.zeros((2,2))
print(array_3)

array_4 = np.full((2,2),9.0)
print(array_4)

array_5 = np.eye(2,2)
print(array_5)

array_6 = np.ones((2,2))
print(array_6)

array_7 = np.random.random((2,3))
print(array_7)