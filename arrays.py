import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
print(arr[1:7])

arr = np.array([[11, 12, 13, 14],
                 [21, 22, 23, 24],
                 [31, 32, 33, 34],
                [41, 42, 43, 44]])
print(arr[[1,2]])
arrs = np.arange(1, 26).reshape(5, 5)
last_col = arrs[:, -1]    # all rows, last column
print(last_col)

lst = [1,2,3,4,5]
result = np.array(lst)
result = result*2
print (result)
newresult = result + result
print(newresult)

#calculate the square of each element in the given lsit using numpy
lst = [1,6,12,8,3,2]
rslt = np.array(lst)
rslt = rslt*rslt
print(rslt)

#access the first  the element in the given list
lst = [1,2,3,4,5]
rslt = np.array(lst)
print(rslt[0])

#access 2D array 
q = [[1,2,3],[4,5,6]]
a = np.array(q)
print(a[1,1])

#3D accessing
a = [[[1,2,3],[4,5,6]], [[8,9,10],[6,5,4]]]
q = np.array(a)
print(q[0,1,1])
print(q[1,0,1])
arrs = np.arange(1, 26).reshape(5, 5)

