import time


class Solver():

    def __init__(self):
        self.gui = None
        self.guiSpeed = .02

    def addVisualizer(self, gui):
        self.gui = gui

    def printGrid(self, grid):
        print("-----------------------")
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                print(val, end=" ")
                if (j + 1) % 3 == 0:
                    print("|", end=" ")  # todo: make the grid printing less gross
            print("")
            if (i + 1) % 3 == 0:
                print("-----------------------")

    def validGrid(self, grid):
        """makes sure grid is a solvable sudoku by checking the validity of each square"""
        for i in range(9):
            for j in range(9):
                val = grid[i][j]
                grid[i][j] = 0
                # removed val from grid to test options properly,
                # since notIn___() returns false for the value at the current index
                options = [testNum for testNum in range(1, 10) if (
                            self.notInRow(grid, i, testNum) and self.notInCol(grid, j, testNum) and self.notInSquare(
                        grid, i, j, testNum))]
                grid[i][j] = val
                if not options or (val and val not in options):
                    # two invalid cases:
                    # no possible correct value at a given index
                    # pre-existing value conflicts with other values in the grid
                    return False
        return True
        # todo: better checks for validity

    def notInRow(self, grid, rowIndex, value):
        """Returns whether the value is found in the same row as the given rowIndex"""
        return value not in grid[rowIndex]

    def notInCol(self, grid, colIndex, value):
        for row in grid:
            if row[colIndex] == value:
                return False
        return True

    def notInSquare(self, grid, rowIndex, colIndex, value):
        for row in range(3 * (rowIndex // 3), 3 * (rowIndex // 3) + 3):
            for col in range(3 * (colIndex // 3), 3 * (colIndex // 3) + 3):
                if grid[row][col] == value:
                    return False
        return True

    def firstEmpty(self, grid):
        for i in range(9):
            for j in range(9):
                if not grid[i][j]:
                    return i, j
        return -1, -1

    def solveSudoku(self, grid, visual = False):
        if self.gui and visual:
            time.sleep(self.guiSpeed)

        r, c = self.firstEmpty(grid)  # get first empty location of the grid
        if r < 0:  # if no empty spaces:
            # solution.extend(grid)
            return True
        for i in range(1, 10):
            if self.notInRow(grid, r, i) and self.notInCol(grid, c, i) and self.notInSquare(grid, r, c, i):
                # print(f"({r},{c}) = {i}")
                if self.gui and visual:
                    self.gui.testValue(r, c, i)
                # ping visualization here to update visual
                grid[r][c] = i
                if self.solveSudoku(grid, visual = visual):
                    if self.gui and visual:
                        self.gui.fixValue(r, c)
                        self.gui.doneSolving()
                    # ping visualization here to show final grid filling
                    return True
                # print(f"({r},{c}) = {0}")
                grid[r][c] = 0
                if self.gui and visual:
                    self.gui.clearValue(r, c)
                # ping visualization here to update visual
        return False


def main():
    s = Solver()
    sudokuGrid = [[0, 0, 0, 0, 0, 0, 2, 0, 0],
                  [0, 8, 0, 0, 0, 7, 0, 9, 0],
                  [6, 0, 2, 0, 0, 0, 5, 0, 0],
                  [0, 7, 0, 0, 6, 0, 0, 0, 0],
                  [0, 0, 0, 9, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 2, 0, 0, 4, 0],
                  [0, 0, 5, 0, 0, 0, 6, 0, 3],
                  [0, 9, 0, 4, 0, 0, 0, 7, 0],
                  [0, 0, 6, 0, 0, 0, 0, 0, 0]]
    s.printGrid(sudokuGrid)
    solution = []
    result = s.solveSudoku(sudokuGrid)
    if not result:
        print("No Solution!")
    else:
        print("Solved:")
        s.printGrid(sudokuGrid)
