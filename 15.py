def create_matrix(n):
    # create an empty matrix
    matrix = [[0 for i in range(n)] for j in range(n)]

    # set start point
    y = 0
    x = -1
    i = 0

    while i <  n ** 2:
        matrix, x, y, i = move_right(matrix, x + 1, y, i, n)
        matrix, x, y, i = move_down(matrix, x, y + 1, i, n)
        matrix, x, y, i = move_left(matrix, x - 1, y, i, n)
        matrix, x, y, i = move_up(matrix, x, y - 1, i, n)

    return matrix


def print_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = ' ')
        print()


def move_right(matrix, x, y, i, n):
    while x < n and matrix[y][x] == 0:
        i += 1
        matrix[y][x] = i
        x += 1
    return matrix, x - 1, y, i


def move_down(matrix, x, y, i, n):
    while y < n and matrix[y][x] == 0:
        i += 1
        matrix[y][x] = i
        y += 1
    return matrix, x, y - 1, i


def move_left(matrix, x, y, i, n):
    while x > -1 and matrix[y][x] == 0:
        i += 1
        matrix[y][x] = i
        x -= 1
    return matrix, x + 1, y, i


def move_up(matrix, x, y, i, n):
    while y > -1 and matrix[y][x] == 0:
        i += 1
        matrix[y][x] = i
        y -= 1
    return matrix, x, y + 1, i
    

n = 4
matrix = create_matrix(n)
print_matrix(matrix, n)
