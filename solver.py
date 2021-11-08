def printGrid(grid):
    print("-----------------------")
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            print(val, end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")  # todo: make the grid printing less gross
        print("")
        if (i + 1) % 3 == 0:
            print("-----------------------")


def validGrid(grid):
    for row in grid:
        if set(row) != (1,2,3,4,5,6,7,8,9):
            return False


def notInRow(grid, rowIndex, value):
    return value not in grid[rowIndex]

def notInCol(grid, colIndex, value):
    for row in grid:
        if row[colIndex] == value:
            return False
    return True

def notInSquare(grid, rowIndex,colIndex,value):
    for row in range(3 * (rowIndex//3), 3 * (rowIndex//3) + 3):
        for col in range(3 * (colIndex//3), 3 * (colIndex//3) + 3):
            if grid[row][col] == value:
                return False
    return True

def firstEmpty(grid):
    for i in range(9):
        for j in range(9):
            if not grid[i][j]:
                return i,j
    return -1,-1

def solveSudoku(grid, solution):
    r,c = firstEmpty(grid) # get first empty location of the grid
    if r < 0: #if no empty spaces:
        solution.extend(grid)
        return True
    for i in range(1,10):
        if notInRow(grid,r,i) and notInCol(grid,c,i) and notInSquare(grid,r,c,i):
            print(f"({r},{c}) = {i}")
            # ping visualization here to update visual
            grid[r][c] = i
            if solveSudoku(grid,solution):
                # ping visualization here to show final grid filling
                return True
            print(f"({r},{c}) = {0}")
            grid[r][c] = 0
            # ping visualization here to update visual
    return False

def main():
    sudokuGrid = [[0, 0, 0, 0, 0, 0, 2, 0, 0],
                  [0, 8, 0, 0, 0, 7, 0, 9, 0],
                  [6, 0, 2, 0, 0, 0, 5, 0, 0],
                  [0, 7, 0, 0, 6, 0, 0, 0, 0],
                  [0, 0, 0, 9, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 2, 0, 0, 4, 0],
                  [0, 0, 5, 0, 0, 0, 6, 0, 3],
                  [0, 9, 0, 4, 0, 0, 0, 7, 0],
                  [0, 0, 6, 0, 0, 0, 0, 0, 0]]
    printGrid(sudokuGrid)
    solution = []
    result = solveSudoku(sudokuGrid,solution)
    if not result:
        print("No Solution!")
    else:
        print("Solved:")
        printGrid(solution)