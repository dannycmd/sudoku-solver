import numpy as np

grid = [[1, 0, 8, 9, 5, 0, 2, 3, 0], 
        [0, 0, 0, 0, 6, 0, 5, 4, 0], 
        [0, 0, 6, 0, 0, 4, 0, 0, 0], 
        [0, 0, 1, 7, 0, 0, 8, 0, 0], 
        [0, 0, 0, 8, 4, 1, 0, 0, 0], 
        [0, 0, 5, 0, 0, 6, 9, 0, 0], 
        [0, 0, 0, 4, 0, 0, 3, 0, 0],
        [0, 1, 9, 0, 3, 0, 0, 0, 0], 
        [0, 2, 4, 0, 7, 8, 6, 0, 1]]

#grid = [[0 for i in range(9)] for i in range(9)]
grid = np.matrix(grid)

def display_grid():
    global grid
    for y in range(9):
        if y % 3 == 0 and y != 9 and y != 0:
            print("---------------------")
        for x in range(9):
            if (x+1) % 3 == 0 and (x+1) != 9:
                print(grid[y, x], "|", end=" ")
            elif (x+1) != 9:
                print(grid[y, x], end=" ")
            else:
                print(grid[y, x])

display_grid()

def possible(y, x, n):
    global grid
    for i in range(9):
        if grid[y, i] == n and i != x:
            return False
    for i in range(9):
        if grid[i, x] == n and i != y:
            return False
    x0, y0 = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i, x0+j] == n and y0+i != y and x0+j != x:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y, x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y, x] = n
                        solve()
                        grid[y, x] = 0
                return
    display_grid()

print("\n")
solve()