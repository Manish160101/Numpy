'''

Function Name - Description
sum(arr)  -> returns sum of all elements in Array
mean(arr) -> Return avg of values, elements in Array
min(arr)  -> returns minimum value from Array
max(arr)  -> Returns max value from Array
std(arr)  -> Calculates standard deviation
var(arr)  -> Calculates Variance

'''

import numpy as np

arr = np.array([10,20,30,40,50])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))