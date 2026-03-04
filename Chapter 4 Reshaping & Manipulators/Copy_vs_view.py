'''

->The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.

->copy owns the data and any changes made to the copy will not affect original array, 
and any changes made to the original array will not affect the copy.

->view does not own the data and any changes made to the view will affect the original array, 
and any changes made to the original array will affect the view.

'''

import numpy as np

#Example of copy
arr_copy = np.array([2,1,6,4,5])
x = arr_copy.copy()
arr_copy[1] = 9   #modifying Original Array but it will not affect x

print(f"Original Array {arr_copy}")
print(f"Copied Array {x}")

#Example of View

arr_view = np.array([1,2,4,6,5])
y = arr_view.view()
arr_view[2] = 9   #Both Arrays will be same now

print(f"Original Array {arr_view}")
print(f"Viewed Array {y}")