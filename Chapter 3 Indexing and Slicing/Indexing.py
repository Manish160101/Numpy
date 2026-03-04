'''
Positive indexing -> 0 to n (Started from left to right)
Negative indexing -> n to -1 (Starts from Right to left)

Syntax:

1-D Array -> arr[index]
2-D Array -> arr[row,column]

If index is out of range -> Raising IndexError

'''

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[2])
print(arr[-1])
