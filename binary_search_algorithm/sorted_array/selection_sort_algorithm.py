import sys


def selectionSort(array):
    reach = len(array)
    current_biggest = -sys.maxsize
    index_current_biggest = 0

    while reach > 0:
        for i in range(reach):
            if array[i] >= current_biggest:
                current_biggest = array[i]
                index_current_biggest = array.index(current_biggest)
            if i == reach - 1:
                array[index_current_biggest], array[reach - 1] = array[reach - 1], array[index_current_biggest]
                current_biggest = array[0]
                reach -= 1


    return array

array = [8, 5, 2, 9, 5, 6, 3]

print(selectionSort(array))
