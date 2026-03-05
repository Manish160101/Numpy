'''
NumPy provides functions to perform log at the base 2, e and 10.
All of the log functions will place -inf or inf in the elements if the log can not be computed.

log with base 2 - > log2()
log with base 10 -> log10()

Natural Log -> log()

frompyfunc(Function, No.of Inputs, No.of Outputs)

'''

import numpy as np
from math import log

arr = np.array([2,4,6,8,10])
arr1 = np.arange(1,11)   #Generates array from 1 to 10

print(np.log2(arr))
print(np.log10(arr1))
print(np.log(arr1))

nplog = np.frompyfunc(log,2,1)

print(nplog(100,10))