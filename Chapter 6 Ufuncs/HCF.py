'''
GCD is also called HCF

GCD -> Greatest Common Divisor

-> Can be checked HCF of Numbers -> gcd() function can be used.
-> Can be Checked HCF of Arrays -> This can be achieved by gcd.reduce() function

'''

import numpy as np

num1 = 10
num2 = 15

print(np.gcd(num1,num2))

arr = np.array([6,4,2])

print(np.gcd.reduce(arr))