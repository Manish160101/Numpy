import numpy

n,m,p = list(map(int,input().strip().split()))

A = numpy.array([list(map(int,input().strip().split())) for _ in range(n)])
B = numpy.array([list(map(int,input().strip().split())) for _ in range(m)])

print(numpy.concatenate((A,B),axis=0))