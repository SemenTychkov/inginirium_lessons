import numpy
arr1 = numpy.arange(10)
arr2 = numpy.arange(20, 20, 20, 20, 20, 5 ,4,3,2,1)
print(arr1)
print(arr2)


def inner(array1, array2):
    for i, e in enumerate(array1):
        if (e in array2) == False:
            return False

    return True

print(inner(array(1, array2))
