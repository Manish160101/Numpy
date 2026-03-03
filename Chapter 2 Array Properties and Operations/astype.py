'''
astype function is used to convert datatypes
syntax:
arr = np.array(["1","2","3"])
print(arr.astype(int))

'''
import numpy as np

arr = np.array(["1","2","3"])
new_arr = arr.astype(int)
print(new_arr)
print(new_arr.dtype)