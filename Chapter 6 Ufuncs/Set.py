import numpy as np

arr1 = np.array([4,3,6])
arr2 = np.array([3,4,6,8])

print(np.setdiff1d(arr2,arr1))
print(np.union1d(arr1,arr2))
print(np.intersect1d(arr1,arr2,assume_unique=True))