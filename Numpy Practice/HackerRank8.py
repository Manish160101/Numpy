'''
Use of min and max

'''
import numpy

N,M = list(map(int,input().strip().split()))

arr = numpy.array([list(map(int,input().strip().split())) for _ in range(N)])

arr_min = numpy.min(arr,axis=0)

arr_max = numpy.max(arr_min)

print(arr_max)