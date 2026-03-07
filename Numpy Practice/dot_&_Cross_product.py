import numpy

N = int(input())

A = numpy.array([[list(map(int,input().strip().split())) for _ in range(N)]]).reshape(N,N)
B = numpy.array([[list(map(int,input().strip().split())) for _ in range(N)]]).reshape(N,N)

print(numpy.dot(A,B))
print(numpy.matmul(A,B))