'''

Ufuncs:- ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
==========================
Vectorization:- Converting iterative statements into a vector based operation is called vectorization.

It is faster as modern CPUs are optimized for such operations.

This eleminates the use of for loop.

Rules:
- Dimension should be same for both arrays to implement ufuncs  [1 2 3] + [3 4 6] => Works
    Eg:
    - [[1 3 5][4 5 6]] + [2 5 6] => Columns are same it will add 
- Single element can be used on all elements of arrays
- Incompatible shapes will lead to throw error
    Eg: 
    - [2 3 5] + [2 5] => Throws error

'''

import numpy as np

arr = np.array([100,200,300,400,500])

new_arr = arr * 10

print(new_arr)

