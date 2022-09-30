import numpy as np


def count_islands(matrix: np.ndarray):
    islands = 0

    rows, cols = matrix.shape
    for row in np.arange(rows):
        for col in np.arange(cols):
            if matrix[row, col] == 0:
                continue
            else:
                islands += 1
                check_nearby(matrix, row, col)
    return islands


def check_nearby(matrix: np.ndarray, row, col):
    rows, cols = matrix.shape
    if row > rows - 1 or col > cols - 1 or row < 0 or col < 0 or matrix[row, col] == 0:
        return

    if matrix[row, col] == 1:
        matrix[row, col] = 0
        check_nearby(matrix, row + 1, col)
        check_nearby(matrix, row, col + 1)
        check_nearby(matrix, row - 1, col)
        check_nearby(matrix, row, col - 1)


M = int(input("M = "))
N = int(input("N = "))
matrix = np.random.randint(2, size=M*N).reshape(N, M)
print(matrix)
print(count_islands(matrix))
