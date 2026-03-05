'''
Broadcasting 1D to 2D Array

'''

import numpy as np

arr1 = np.array([[2,5,6],[8,5,2]])
arr2 = np.array([4,7,2])   # Numpy automatically expands it to both rows

result = arr1 + arr2
print(result)