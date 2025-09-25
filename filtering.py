import numpy as np
marks = np.array([45,78,23,90,67,88,34,59])
arr = marks[marks>50]
print(arr)
print(arr.sum())

arr = np.array([12,45,67,89,34,22,90,100])
new = arr[(arr>40) & (arr<90)]
print(new.mean())

arr =np.array([[20,30,40,50],
               [60,70,80,90],
               [25,65,75,85]])
new = arr[arr>50]
print(new)
print(new.max())

data = np.array([120,56,89,45,38,99,140,110])
new = data[data<100]
print(new)
print(new.min())
array = np.array([[10,20,30],
                  [40,50,60],
                  [70,80,90]])
new =array[array>30]
new = array[array<80]
print(new)
print(new.sum())

scores = np.array([34,56,78,90,45,66,89,91,50])
new = scores[scores>60]
print(new)
print(new.mean())
print(scores.size)

