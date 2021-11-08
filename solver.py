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
        print("No empty spaces left! Sudoku is solved!")
        solution.extend(grid)
        return True
    for i in range(1,10):
        if notInRow(grid,r,i) and notInCol(grid,c,i) and notInSquare(grid,r,c,i):
            grid[r][c] = i
            if solveSudoku(list.copy(grid),solution):
                print(f"filling space {r},{c} with {i}")
                return True
            grid[r][c] = 0
    return False

def main():
    sudokuGrid = [[0, 7, 0, 0, 0, 8, 0, 0, 0],
                  [0, 0, 0, 0, 0, 9, 7, 4, 0],
                  [8, 4, 0, 2, 0, 0, 0, 6, 0],
                  [1, 0, 0, 0, 0, 6, 0, 0, 0],
                  [3, 9, 0, 0, 0, 0, 0, 8, 5],
                  [0, 0, 0, 3, 0, 0, 0, 0, 1],
                  [0, 2, 0, 0, 0, 4, 0, 9, 3],
                  [0, 5, 8, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 5, 0, 0, 0, 1, 0]]
    solution = []
    result = solveSudoku(sudokuGrid,solution)
    if not result:
        print("No Solution!")
    else:
        for row in solution:
            for val in row:
                print(val,end=" ")
            print("\n")