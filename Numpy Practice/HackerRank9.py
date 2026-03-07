import numpy

N,M = list(map(int,input().strip().split()))

arr = numpy.array([list(map(int,input().strip().split())) for _ in range(N)])

print(numpy.mean(arr, axis=1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr),11))