'''
- Append helps in adding value at the end of an Array
- Creates a new array
- Syntax is same as insert

'''

import numpy as np

arr = np.array([2,3,5])

new_arr = np.append(arr,[2,5,7])

print(new_arr)   #[2 3 5 2 5 7]