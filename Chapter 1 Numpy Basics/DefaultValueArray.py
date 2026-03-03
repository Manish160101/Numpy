'''
Numpy provides few methods to print array with default value
    arr = np.ones(shape)  shape -> size of array -> prints 1s
    arr = np.zeros(shape)  -> prints zeros
->shape uses Tuples
->to print multi dimensional array pass size in tuple => array((2,4))  -> it will print 2 rows 4 column array

-> Instead of printing 1s and 0s, print specific value using full function

full(shape, value)


'''

import numpy as np

arr = np.ones((2,3))
arr1 = np.zeros(2)
arr2 = np.full(3,2)    # [2 2 2]
arr3 = np.full((2,3),4)   # it will print multidimensional array with value only 4 in all

print(arr)
print(arr1)
print(arr2)
print(arr3)