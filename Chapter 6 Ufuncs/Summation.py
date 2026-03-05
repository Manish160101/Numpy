import numpy as np

arr = np.array([[2,4,7],[8,2,5]])

print(np.sum(arr)) # Sum of all elements
print(np.sum((arr),axis=1))  #Adds each row and print new Array [13 15]
print(np.sum((arr),axis=0))  #Adds each column and print new Array [10 6 12]

'''
Cummulative Sum:
The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
'''

arr1 = np.array([1,2,3,5,6])
print(np.cumsum(arr1))


