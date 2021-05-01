import numpy as np

grid = []
with open("input.txt") as textFile:
    for line in textFile:
        each_line = [item.strip() for item in line.split(',')]
        input_line = [int(item) for item in each_line]
        grid.append(input_line)
print(grid)


def possible(row, column, number):
    global grid

    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == number:
                return False

    return True


def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    np.savetxt('result.txt', grid, fmt='%d')

    print(np.matrix(grid))


solve()
