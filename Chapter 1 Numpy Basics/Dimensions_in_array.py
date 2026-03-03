'''
Array can be of multiple dimensions

0D - np.array(2)
1D - np.array([1,2,4,5])
2D - np.array([[1,2,3],
                [1,3,4]])
3D - np.array([[[1,2,3],
                [2,4,6]],

                [[2,3,5],
                [2,3,7]]])
            
Dimensions can be checked using ndim Attribute.
Array Dimensino can be defined using ndmin as argument in array

arr = np.array([2,3,4,5],ndmin=3) -> It will create 3 Dimentional array

we can check dimensions of array using ndim
print(arr.ndim)

'''

import numpy as np

a = np.array(2)
b = np.array([1,2,4,5,6])
c = np.array([[1,2,4],[2,3,5]])
d = np.array([[[1,2,4],
             [2,3,5]],
             [[2,3,8],
              [4,6,2]]]
             )

arr = np.array([1,2,4,6,6,3,23,5,6], ndmin=2)


print(a.ndim)    #0Dimension
print(b.ndim)    #1Dimension
print(c.ndim)    #2Dimension
print(d.ndim)    #3Dimension

print(arr)