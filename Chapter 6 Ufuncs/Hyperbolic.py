'''
NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians 
and produce the corresponding sinh, cosh and tanh values..

np.pi -> gives value of pi

'''
import numpy as np

print(np.sinh(1))
print(np.cosh(1))
print(np.tanh(1))

arr = np.array([0.1, 0.2, 0.5])

print(np.arctanh(arr))
print(np.arcsinh(arr))