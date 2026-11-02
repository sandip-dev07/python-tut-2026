# Use list by default for everyday tasks, web dev, or mixed-data collections.

# Use numpy.ndarray if you are doing math, working with matrices, or handling large numerical datasets.

# Use the built-in array module only if you need a memory-efficient 1D array and cannot install external libraries like NumPy.

from array import *

arr1 = array('i', [1, 2, 3, 4, -15])
print(arr1)
# print(type(arr1))

arr2 = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print(arr2)


# arr2.append(6.6)
# print(arr2)

# arr2.insert(1, 7.7)
# print(arr2)

# arr2.pop()
# print(arr2)


# arr3 = array(arr2.typecode, arr2.tolist()) # extra space
arr3 = array(arr2.typecode, (i for i in arr2))
arr2[2] = 9.9

print(arr2)
print(arr3)