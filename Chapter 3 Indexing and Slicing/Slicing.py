'''
Slicing:

Accessing sub part of array.

Syntax:

arr[Start,Stop,Step]

- element in place of stop will be ignored
- By default step is 1

'''

import numpy as np

arr = np.array([1,4,3,2,5])

print(arr[::-1])
print(arr[1:5])