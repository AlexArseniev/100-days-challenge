def spiralTraverse(array):

    array_to_return = []

    while array:
        array_to_return += array.pop(0)
        array = list(zip(*array))[::-1]

    return array_to_return

    output = []
    start_row = 0
    start_col = 0
    end_row = len(array)
    end_col = len(array[0])

    while start_row < end_row and start_col < end_col:
        # right
        for i in range(start_col, end_col):
            output.append(array[start_row][i])
        start_row += 1
        # down
        for i in range(start_row, end_row):
            output.append(array[i][end_col - 1])
        end_col -= 1
        # left
        for i in range(end_col - 1, start_col - 1, -1):
            output.append(array[end_row - 1][i])
        end_row -= 1
        # up
        for i in range(end_row - 1, start_row - 1, -1):
            output.append(array[i][start_col])
        start_col += 1

    return output



array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]

print(spiralTraverse(array))

