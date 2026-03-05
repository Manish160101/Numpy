'''
Insert function for 2-D Array

'''

import numpy as np

arr = np.array([[1,3],[4,2]])

new_arr = np.insert(arr, 2, [5,3], axis=0)
print(new_arr)

new_arr1 = np.insert(arr,2,[5,3],axis = 1)
print(new_arr1)

flat_arr = np.insert(arr,1,[6,3],axis= None)
print(flat_arr)