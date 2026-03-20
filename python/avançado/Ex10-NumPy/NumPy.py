import numpy

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
arr = numpy.array([1, 2, 3, 4])
print(arr[0])
arr = numpy.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
arr = numpy.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
arr = numpy.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
arr = numpy.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('forma do array:', arr.shape)