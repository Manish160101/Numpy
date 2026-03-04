'''
Deleting elements from 2 D Array

'''

import numpy as np

arr = np.array([[5,3,1],[6,7,9]])

new_arr = np.delete(arr, 0, axis=0)

print(new_arr)