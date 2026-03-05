'''
inf -> infiniity

isinf() -> to check if any value is infinite in Array like: 1/0=Infinite

'''

import numpy as np

arr = np.array([2,5,6,3,np.inf,4,-np.inf])

print(np.isinf(arr))

