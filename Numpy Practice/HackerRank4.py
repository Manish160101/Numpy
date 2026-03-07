import numpy as np
n,m = list(map(int,input().strip().split()))

A = np.array([list(map(int,input().strip().split())) for _ in range(n)])

arr_sum = np.sum(A,axis=0)
print(np.prod(arr_sum))

#A = np.array([1,3])
#B = np.array([2,3])

# new_arr = np.array([A,B])





