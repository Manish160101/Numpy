import numpy as np

def arrays(arr):
    x = np.array(arr, float)
    return x[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
