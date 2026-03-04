'''
To join two arrays we need to use Concatenate function
np.concatenate((Array1,Array2),axis = num)

num = 0,1,None

0 > Row Wise Stacking (Vertical Stacking)
1 > Column wise stacking (Horizontal Stacking)


'''

import numpy as np

arr1 = np.array([2,4,3])
arr2 = np.array([7,6,4])

x = np.concatenate((arr1,arr2))
print(x)   #[2 4 3 7 6 4]

