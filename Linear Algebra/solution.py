import numpy
n= int(input())
matrix=[]
for i in range(n):
    matrix.append((list(map(float,input().split()))))
print(round(numpy.linalg.det(matrix),2))
