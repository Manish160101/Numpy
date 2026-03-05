'''



'''

import numpy as np

arr1 = np.array([[2,4,6],[5,6,2]])

print(np.prod(arr1))    #product of all elements
print(np.prod((arr1),axis=1))  # product of all elements in each row and return new Array [48 60]
print(np.prod((arr1),axis = 0)) #produc of all elements in each columns and returns new Array [10 24 12]

'''
Cummulative product means taking the product partially.

E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
'''
arr2 = np.array([5,6,2])
print(np.cumprod(arr2))   #[5 30 60]