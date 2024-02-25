import numpy

arr = numpy.empty([2,2], dtype=int)
print(arr)

arr2 = numpy.ones([2,2], dtype=int)
print(arr2)
arr3 = numpy.arange(10)
print(arr3)
print(arr3[slice(2, 7, 2)])
print(arr3[::])