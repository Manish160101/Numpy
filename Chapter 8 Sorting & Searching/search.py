'''
Searching of value can be achieved using where() function.
It returns the Array of index number of specified value

'''

import numpy as np

arr = np.array([5,32,5,7,4,7,8])

x = np.where(arr == 7)

print(x)