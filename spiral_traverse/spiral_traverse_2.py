def spiralTraverse(array):
    array_to_return = []

    while array:
        array_to_return += array.pop(0)
        array = list(zip(*array))[::-1]

    return array_to_return


array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]

print(spiralTraverse(array))

