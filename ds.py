import numpy as np
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