'''
We can insert value at specific position by using in build function called insert()

Syntax:

np.insert(Array, Index_no, Value, axis)

Axis Values:

1-D Array
None

2-D Array:
Axis = 0 if want to start row wise  (By default it's row wise)
Axis = 1 if want to start column wise
Axis = Non -> This flattens the Array

'''
import numpy as np

try:
    arr = np.array([1,2,4,5,3])

    x = np.insert(arr,5,8)   

    print(x)    #output -> [1 2 4 5 3 8]

except IndexError:

    print("Wrong Index no")