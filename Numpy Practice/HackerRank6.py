import numpy as np

n,m = tuple(map(int,input().strip().split()))

arr = np.array([list(map(int,input().strip().split())) for _ in range(n)])

print(arr.transpose())
print(arr.flatten())