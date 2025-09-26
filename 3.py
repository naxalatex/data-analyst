import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
new = arr.reshape(4,2)
print(new)

arr = np.array([[10,20], [30,40],[50,60]])
new = arr.flatten()
print(new)

arr = np.array([[1,2,3],[4,5,6]])
new = arr.ravel()
print(new)

arr = np.array([[1,2,3],[4,5,6]])
new = arr.transpose()
print(new)

a = np.array([[10,20,30]])
b = np.array([[40,50,60]])
new = np.concatenate((a,b), axis =0)
print(new)

a = np.array([1,2,3])
b = np.array([4,5,6])
new = np.stack((a,b))
new = np.stack((a,b),axis = 1)
print("horizantal:", new)
print("verticsal:",new)

arr = np.array([5,10,15,20,25,30])
new = np.split(arr,3)
print(new)

arr = np.array([[1,2],[3,4],[5,6],[7,8]])
new = np.split(arr,2)
print(new)

a = np.array([2,4,4,2,5,5,7,7,7])
new = np.unique(a)
print(new)

arr = np.array([[1,2,2],[3,4,4],[5,6,6]])
new = arr.flatten()
new = np.unique(arr)
new = np.reshape(2,-1)
new = print(new)
