import numpy as np
a = np.arange(1,11)
b = np.arange(1,11)
mult= a[:,None]*b
print(mult)

#reshape
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape(2,3)
print("reshaped():\n",reshaped)

#flatten
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
flat = arr.flatten()
print("flatten():\n",flat)

#ravel
arr = np.array([[10,20],[30,40]])
ravelled = arr.ravel()
print("ravel():\n", ravelled)

#transpose
arr = np.array([[1,2,3],[4,5,6]])
transposed = arr.transpose()
print("transpose:", transposed)

#concatenate
arr = np.array([1,2,3])
b = np.array([4,5,6])
joined = np.concatenate((arr,b))
print("concatenate:", joined)
#2D exmple
A = np.array([[1,2],[3,4]])
B = np.array([[5,6]])
C = np.concatenate((A,B), axis=0)
print("2D concatenate:\n", C)   

#vstack
a = np.array([1,2,3])
b = np.array([4,5,6])
vertical = np.vstack((a,b))
horizontal = np.hstack((a,b))
print("vstack:\n", vertical)
print("hstack:", horizontal)
 
#split
arr = np.array([10,20,30,40,50,60])
parts = np.split(arr,3)
print("split:", parts)

#unique
arr = np.array([1,2,2,3,3,4,4,5])
unique_values = np.unique(arr)
print("unique:", unique_values) 