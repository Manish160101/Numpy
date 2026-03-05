'''
There is a method called searchsorted() which performs a binary search in the array, 
and returns the index where the specified value would be inserted to maintain the search order.

'''

import numpy as np

arr = np.array([6,7,8,9])
x = np.searchsorted(arr, 9)
print(x)

# we can search from right as well

y = np.searchsorted(arr,9, side='right')   
print(y)  #It will show on which index value 10 can be inserted.

z = np.searchsorted(arr,[10,4], side='right') 
print(z)  # This will show array of Index for both the values passed in above list