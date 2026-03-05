'''
sin(), cos(), tan()

'''
import numpy as np

values = np.array([1,0.5,0])

print(np.arcsin(values))
print(np.rad2deg(np.arcsin(values)))

print(np.arccos(values))
print(np.rad2deg(np.arccos(values)))

print(np.arctan(1))
print(np.rad2deg(np.arctan(1)))

Base, Height = 5,10

print(np.hypot(5,10))    #hypot(Base,Height)

