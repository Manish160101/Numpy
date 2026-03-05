'''
NaN -> Not a Number

to find a Nan values we use isnan(arr) function.
it returns Boolean value


'''

import numpy as np

arr = np.array([2,5,6,np.nan,5])

print(np.isnan(arr))
