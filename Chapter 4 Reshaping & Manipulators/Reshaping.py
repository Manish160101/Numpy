'''
Reshaping means changing the Array dimension without changing it's data

1 - D to 2-D array

[1,2,3,4]  -> [[1 2][2 3]]

reshape((rows,column))
rows * column = No. of Elements -> Should satisfy this to use reshape function

Reshaping returns view not copy

'''

import numpy as np

arr = np.array([1,2,3,5,6,7])

x = arr.reshape((3,2))

print(x)