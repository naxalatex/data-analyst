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

