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