'''
If NaN value found we can convert it num

Syntax -> nan_to_num(Array, nan=value) default = 0

for Infinity
nan_to_num(Array, posinfo=value, neginfo=value)
posinfo => for Positive value
neginfo => for Negative value
'''

import numpy as np

#Converting Nan to Num

arr = np.array([2,4,5,np.nan,6])

print(np.nan_to_num(arr,nan=4))


#Converting Infinite value to Num

arr1 = np.array([2,5,np.inf,5,6, -np.inf])
print(np.nan_to_num(arr1, posinf=50, neginf=-30))