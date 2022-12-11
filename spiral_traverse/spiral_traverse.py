'''
Write a function that takes in an n x m
two-dimentional array and returns a one-dimentional array
of all the array's elements in spiral order.
'''


def spiralTraverse(array):
    current_len_column = len(array)
    current_len_row = len(array[0])
    current_start = 0
    current_end = 0
    start_column = 0
    end_row = 0

    array_to_return = []

    total_nums = sum([len(item) for item in array])

    while len(array_to_return) < total_nums:
        start_column = current_start
        end_row = current_end
        # move right
        for i_move_right in range(current_len_row):
            array_to_return.append(array[end_row][start_column])
            start_column += 1
        if len(array_to_return) == total_nums:
            break
        # move down
        end_row += 1
        for i_move_down in range(1, current_len_column):
            array_to_return.append(array[end_row][start_column - 1])
            end_row += 1
        # move left
        start_column -= 1
        for i_move_left in range(1, current_len_row):
            start_column -= 1
            array_to_return.append(array[end_row - 1][start_column])
        # move up
        end_row -= 1
        for i_move_up in range(1, current_len_column - 1):
            array_to_return.append(array[end_row - 1][start_column])
            end_row -= 1

        current_start += 1
        current_end += 1
        current_len_column -= 2
        current_len_row -= 2

    return array_to_return


array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]

# Expected output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(spiralTraverse(array))
