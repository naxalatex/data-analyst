import numpy as np
arrays = np.array([1,2,3,4,5])
print(arrays +1)
print(arrays -1)
print(arrays *2)
print(arrays /4)
print(arrays **3)

#vector arithmetic (1D array) mathematical operaition on arrays
#If you us5e a function that works on each elements  of a vector - also vector operation

array = np.array([1,2,3,4,5,6])
array1 = np.array([1.0,2.3,5,1,8.6])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.pi)

#element eise arithmetic

array1 = np.array([1,2,3,4,5,])
array2 = np.array([6,7,8,9,1])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

#Element wise arithmetic
A = np.array([[1,2],
             [3,4]])
B = np.array([[5,6],
              [7,8]])

print (A * B)
arr = np.array([[100,200,300],
                [400,500,600],
                [700,800,900]])
print(arr[[1,0,1]])