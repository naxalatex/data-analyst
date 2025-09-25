import numpy as np
arr = np.array ([[1,2,3,4,5],
                [6,7,8,9,10]])

print("sum of all elements",np.sum(arr,axis =0))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.sum(arr,axis=1))
print(np.prod(arr))