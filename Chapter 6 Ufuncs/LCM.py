'''
LCM -> Lowest Common Multiple

-> Can be checked LCM of Numbers -> lcm() function can be used.
-> Can be Checked LCM of Arrays -> This can be achieved by lcm.reduce() function

'''
import numpy as np

#For Numbers
num1 = 5
num2 = 10
print(np.lcm(num1,num2))

# For Arrays
arr = np.array([4,5,6])
print(np.lcm.reduce(arr))