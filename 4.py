import numpy as np
arrays = np.array([1,2,3,4,5,6,7,8,9])
result = arrays[arrays>6]
print(result)

arrays = np.array([[1,2],[3,4],[5,6]])
result = arrays.flatten()
print(result)

arrays = np.array([[1,2,3],[4,5,6],[7,8,9]])
new = arrays.transpose()
print(new)

array= np.array([[1,2,3,4]])
b = np.array([[5,6,7,8]])
new = np.concatenate((array,b),axis = 0)
print(new)