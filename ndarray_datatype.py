import numpy as np
ex1 = np.array([11,12],dtype=np.int64)
print(ex1)
print(ex1.dtype)
print()
ex2 = np.array([11,12],dtype=np.float64)
print(ex2)
print(ex2.dtype)
print()
ex3 = np.array([11.4,12.6],dtype=np.int64)
print(ex3)
print(ex3.dtype)
print()

x = np.array([[111,112],[121,122]],dtype=np.int)
y = np.array([[211.1,212.1],[221.1,222.1]],dtype=np.float64)
print(x)
print()
print(y)
print()

print(x + y)
print()
print(np.add(x, y))
print()

print(x - y)
print()
print(np.subtract(x, y))
print()

print(x * y)
print()
print(np.multiply(x, y))
print()

print(x / y)
print()
print(np.divide(x, y))
print()


print(np.sqrt(x))
print()

print(np.exp(x))
print()
