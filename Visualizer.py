import tkinter as tk


class Visualizer:
    solver = None

    def __init__(self, solver):
        self.solving = False

        # if type(solver) != "Solver":
        #     raise TypeError("solver parameter must be a Solver-type object")
        self.solver = solver

        self.root = tk.Tk()
        self.root.geometry("500x700")
        buttonFrame = tk.Frame(self.root, width=500, height=200, bg="blue")
        buttonFrame.pack(side=tk.BOTTOM)
        solveButton = tk.Button(buttonFrame, width=10, height=5, command=self.solve)
        solveButton.pack()
        resetButton = tk.Button(buttonFrame, width=10, height=5, command=self.reset)
        resetButton.pack()

        self.buttonGrid = []
        self.grid = []
        sudokuFrame = tk.Frame(self.root, width=500, height=500, bg="yellow")
        for i in range(9):
            sudokuFrame.columnconfigure(i, weight=1, minsize=5)
            sudokuFrame.rowconfigure(i, weight=1, minsize=3)
            row = []
            for j in range(9):
                sudokuSquare = tk.Text(sudokuFrame, bg="white")
                row.append(sudokuSquare)
                sudokuSquare.grid(column=j, row=i)
            self.buttonGrid.append(row)
        sudokuFrame.pack()

    def setSolver(self, solver):
        self.solver = solver

    def extractText(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.buttonGrid[i][j].get("1.0", "end-1c")
                row.append(int(val) if len(val) > 0 else 0)
            grid.append(row)
        self.grid = grid
        print(grid)

    def solve(self):
        if not self.solver:
            raise AttributeError("Solver not initialized for Visualizer object")
        self.solving = True
        self.extractText()
        solution = []
        self.solver.solveSudoku(self.grid, solution)
        self.solving = False
        self.grid = solution
        print(solution)

    def fixValue(self, row, col):
        print("Fix value called")
        #self.buttonGrid[row][col].configure(bg="green")

    def testValue(self, row, col, value):
        print("Test Value called")
        self.buttonGrid[row][col].insert("1.0", str(value))
        #self.buttonGrid[row][col].configure(bg="red")

    def clearValue(self, row, col):
        print("Clear value called")
        self.buttonGrid[row][col].delete("1.0", tk.END)
        #self.buttonGrid[row][col].configure(bg="white")

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.clearValue(i, j)

    def start(self):
        self.root.mainloop()

