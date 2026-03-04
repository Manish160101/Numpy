'''
- np.delete(Array, index_no, Axis = None) -> helps in deleting value from specific position
- It creates new arraya after deletion and keep original untouched
'''


import numpy as np

arr = np.array([4,6,2,1,7])

new_arr = np.delete(arr, 1)

print(new_arr)