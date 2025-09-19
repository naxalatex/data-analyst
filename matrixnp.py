import numpy as np

A =np.array([[1,2],
            [3,4]])

B =np.array([[5,6],
            [7,8]])

print(np.matmul(A,B))
print(A@B)
print(A.dot(B))


C = np.array([[2],
             [4],
             [6]])

D = np.array([[1,2,3]])
#
print(C@D)
print(C.dot(D))
print = (np.matmul(C,D))


