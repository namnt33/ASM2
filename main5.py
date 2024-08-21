import numpy as np
#create array : Tao mang 1 chieu
arr1 = np.array([1,2,3,4,5,6,7])

#create 2D array : Tao mang 2 chieu

arr2 = np.array([1,2,3],[4,5,6])

arr_zeros = np.zeros((3,4))
arr_ones = np.ones((3,4))
print(arr_zeros)
print(arr_ones)

arr_range = np.arange(0,10,2)
print(arr_range)
arr_add = arr_range + 5
print(arr_add)

array_test = [1,2,3,4,5,6]
array_shape = np.reshape(array_test, (2,3))
print(array_shape)

