#aggregate functions
import numpy as np
arr=np.array([[50,60,40,89,90],
       [89,78,56,75,99]])
arrays = arr[arr>40]
print(arrays)
marks = arr[(arr>40) &(arr<90)]
print(marks)
marks = arr[(arr<50)|(arr>90)]
print(marks)
updated_marks = arr[~(arr>40) &(arr<90)] #(`~` works opposite to &)
print(updated_marks)

marks = np.array([45,78,23,90,67,88,34,59])
arr = marks[marks>50]
print(arr)
print(arr.sum())

