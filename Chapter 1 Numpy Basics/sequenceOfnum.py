'''
To print sequence of numbers use arange function same as range()
arange(start,end,step)

'''

import numpy as np

a = np.arange(1,10,2)

for i in a:
    print(f"Odd Numbers are {i}")

for i in np.arange(2,11,2):
    print(f"Even Numbers are {i}")