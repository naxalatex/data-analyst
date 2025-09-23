# taking elements from one given index to another given index is called slicing
import numpy as np
arr = np.arraylst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[1:8])
print(arr[1:])
print(arr[:1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
print(arr[::3])

nested_lst = [
    [1, 2, 3, 5, 9, 8],
    [4, 5, 6, 7, 8, 9]


]

new_arr = np.array(nested_lst)
print( new_arr[1, 0:4])
print(new_arr[0:2,1])
print(new_arr[0:2 , 1:4])

arr = np.array([10,20,30,40,50,60,70,80])
print(arr[2:5])
print(arr[0:5])
print(arr[0:4])
print(arr[-3:])
print(arr[-3:-2])

# 1. Given the array:
# arr = np.array([10, 20, 30, 40, 50, 60])
# → Extract elements from index 2 to 4.

arr = np.array ([10,20,30,40,50,60])
print(arr[2:4])

# 2. Given the 2D array:
# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]])
# → Slice out the subarray containing [[6, 7], [10, 11]].

arr = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])
print(arr[[[1,2]]])

arr = np.arange(1,21).reshape(4,5)
print(arr)
result = arr[2:, :3]
print(result)

import numpy as np

arr = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print(arr)
second_col = arr[:, 1]
print(second_col)
import numpy as np

arr = np.arange(30)  # 0 to 29
print(arr)

every_third = arr[::3]
print(every_third)
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])
result = np.dot(A, B)
# or
# result = A @ B
print(result)
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = A @ B   # matrix multiplication
print(result)
A = np.array([[2, 0],
              [1, 3]])

B = np.array([[1],
              [4]])
C = A @ B
print(C)