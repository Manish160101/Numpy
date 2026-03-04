'''
Flattening of Array -> Used to convert Multidimensional Array into 1-D array

There are two functions to achieve that.

.ravel() -> returns view

.flatten() -> returns copy

another method is using reshape.
.reshape(-1) # this also converts multidimension to 1D
'''

import numpy as np

arr = np.array([[1,2,4],[6,6,3]])

print(arr.ravel())
print(arr.flatten())
print(arr.reshape(-1))