import numpy as np

arr = np.array([25,5,10,15])

print(np.diff(arr))   #Return difference of two successive elements and given new Array, [10-5 15-10] => [5 5]

'''
also we can check diff in n number of times.
if n =2 
arr = [25, 5, 10, 15]
returns [5-20 10-5 15-10] => [-20 5 5]
again [5-(-20) 5-5] => [25 0]

'''

print(np.diff((arr),n=2))   

