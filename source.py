def get_row(board, index):
    return board[index]


def get_col(board, index):
    return [x[index] for x in board]


def get_square(board, row, col, offset=3):
    res_rows = board[row * offset : (row + 1) * offset]
    result = [x[col * offset : (col + 1) * offset] for x in res_rows]
    return [val for sublist in result for val in sublist]


def is_there_repetition(lst):
    return len(set(lst)) != len(lst)


def done_or_not(board): #board[i][j]
    for i in range(9):
        if is_there_repetition(get_row(board, i)) or is_there_repetition(get_col(board, i)):
            return 'Try again!'
    for i in range(3):
        for j in range(3):
            if is_there_repetition(get_square(board, i, j)):
                return 'Try again!'
    return 'Finished!'


b = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

print done_or_not(b)


