'''
There are primarily five ways of rounding off decimals in NumPy:

truncation -> Removes values after Decimals
fix -> Removes values after Decimals (Deprecated)
rounding -> Rounding to specified number of places, If >=5 add 1 or do nothing
floor  -> Nearest Lower Integer
ceil  -> Nearest Greater Integer

'''
import numpy as np

arr1 = np.array([54.356, 23.2223, 76.6674])

print(np.trunc(arr1))
print(np.round(np.sum(arr1),2))
print(np.floor(arr1))
print(np.ceil(arr1))



