# from dumpy import Mat
# from dumpy import MatZeros
# from dumpy import MatOnes
# from dumpy import MatRandom

from dumpy import *
import random

# Try printing a matrix
A = Mat([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9],
    [10,11,12,13,14,15]
])

B = Mat([
    [10,11,12,13,14,15],
    [4,5,6,7,8,9],
    [1,2,3,4,5,6]
])

D = Mat([
    [1, 2, 3],
    [6, 7, 8],
    [2, 3, 4]
])

X = MatZeros([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9],
    [10,11,12,13,14,15]
])
Y = MatOnes([
    [10,12,13,14,15,16],
    [4,5,6,7,8,9],
    [10,11,12,13,14,15]
])
Z = MatRandom([
    [random.random() for _ in range(6)],
    [random.random() for _ in range(6)],
    [random.random() for _ in range(6)]
])

print("\nMatrix A")
print(A)

result = A.add()
print("Result of M + 2:")
print(result)

radd = A.__radd__()
print("Result of 2 + M: ")
print(radd)

result_A = A.addMMZ(X)
result_B = B.addMMZ(X)
print("\nResult of Mat + MatZeros: ")
print(result_A)
print(result_B)

resultmmo1 = A.addMMO(Y)
resultmmo2  = B.addMMO(Y)
print("\nResult of Mat + MatOnes: ")
print(resultmmo1)
print(resultmmo2)

resultmmr1 = A.addMMR(Z)
resultmmr2 = B.addMMR(Z)
print("\nResult of Mat + MatRandom: ")
print(resultmmr1)
print(resultmmr2)

# # M + 2 == 2 + M
# result=A.scalar_operation()
# print("\nResult: ")
# print(result)

C = A.transpose()
print("\nMatrix A.transpose()")
print(C)

print("\nMatrix A shape")
print(A._shape())

C = A + B
print("\nMatrix A+B")
print(C)

C = A - B
print("\nMatrix A-B")
print(C)

C = A * B
print("\nMatrix A*B")
print(C)

C = A / B
print("\nMatrix A/B")
print(C)

C = A // B
print("\nMatrix A//B")
print(C)

C = A @ B
print("\nMatrix A@B")
print(C)

C = A.transpose() @ B
print("\nMatrix A.transpose()@B")
print(C)

A.flatten()
print("\nMatrix A flatten")
print(A)

det = D.determinant()
print("\nResult of determinant: ")
print(det)

inverse = D.inverse()
print("\nResult of inverse: ")
print(inverse)