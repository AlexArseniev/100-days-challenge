'''
Determines the index of the searched value in sorted array using binary search
'''
import copy
import math


def binarySearch(array, target):

    if target not in array:
        return -1

    middle = math.floor(len(array) / 2)
    current_array = copy.copy(array)

    while middle > 0:
        if target > current_array[middle]:
            current_array = current_array[middle:]
        elif target < current_array[middle]:
            current_array = current_array[:middle]
        else:
            return array.index(current_array[middle])
        middle = math.floor(len(current_array) / 2)
        if middle == 0:
            return array.index(current_array[0])



array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
# Expected output 3
print(binarySearch(array, target))
