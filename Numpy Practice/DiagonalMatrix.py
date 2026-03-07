import numpy
#numpy.set_printoptions(legacy='1.13')

a = tuple(map(int,input().split()))
y = numpy.eye(a[0],a[1])
print(y)