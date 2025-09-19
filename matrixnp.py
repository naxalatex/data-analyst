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

#Calculate area of circles wuth each elements (radius) in an array using numpy(area if circle = pi r**2)
# arr = [1,2.5,3,7,3.2]
arr =np.array ([[1,2.5,3,7,3.2]])
area = np.pi * arr**2
print("area:",area)
print("arr:",area)
