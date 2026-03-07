import numpy
size = tuple(map(int,input().strip().split()))

A = numpy.array([list(map(int,input().strip().split())) for _ in range(size[0])]).reshape(size[0],size[1])
B = numpy.array([list(map(int,input().strip().split())) for _ in range(size[0])]).reshape(size[0],size[1])

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))
