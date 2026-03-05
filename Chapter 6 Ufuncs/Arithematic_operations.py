import numpy as np

arr1 = np.array([5,10,15,20])
arr2 = np.array([2,4,6,8])

print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))
print(np.mod(arr1,arr2))
print(np.remainder(arr1,arr2))  # same as mod
print(np.power(arr1,arr2))
print(np.divmod(arr1,arr2))  # returns Quoatient(First Array) and Remainder(Secondary Array)

arr3 = np.array([-1,-4,-5])
print(np.absolute(arr3))     # Returns positive numbers
