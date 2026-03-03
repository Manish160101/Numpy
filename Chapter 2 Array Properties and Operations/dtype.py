'''
dtype is used to get data type of elements store in Array
Eg: 

arr = np.array([1,2,3])

print(arr.dtype)   #int64 -> int is datatype and 64 is bit size


dtype can also be used to do typecasting of Array, we can use astype function as well.
Eg:
arr = np.array([1,2,3],dtype = float)  #now elements will be converted to float. #[1. 2. 3.]

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

'''

import numpy as np

arr = np.array([1,2,4,5])
arr1 = np.array([1,2,4,5], dtype = float)
print(arr.dtype)   #int64
print(arr1)    #[1. 2. 4. 5.]