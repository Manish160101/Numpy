'''
Two functions available in Stacking

vstack() -> Increasing rows
hstack() -> Increasing Columns

'''

import numpy as np

arr1 = np.array([5,6,3])
arr2 = np.array([7,2,1])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

