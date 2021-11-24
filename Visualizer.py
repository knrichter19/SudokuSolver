import tkinter as tk
from tkinter import messagebox

class Visualizer:
    solver = None

    def __init__(self, solver):
        self.solving = False

        self.solver = solver

        self.root = tk.Tk()
        self.root.title("Sudoku Solver")
        self.root.geometry("500x700")
        buttonFrame = tk.Frame(self.root, width=500, height=200, bg="blue")
        buttonFrame.pack(side=tk.BOTTOM)
        solveButton = tk.Button(buttonFrame, width=10, height=5, command=self.solve, text = "Solve")
        solveButton.grid(column=0, row=0)
        visualButton = tk.Button(buttonFrame, width=30, height=5, command=lambda: self.solve(visual=True),
                                 text="Solve (visual, slow)")
        visualButton.grid(column=1, row=0)
        resetButton = tk.Button(buttonFrame, width=10, height=5, command=self.reset, text = "Reset")
        resetButton.grid(column=2, row=0)

        self.buttonGrid = []
        self.grid = []
        sudokuFrame = tk.Frame(self.root, width=500, height=500, bg="yellow")
        for i in range(9):
            sudokuFrame.columnconfigure(i, weight=1, minsize=5)
            sudokuFrame.rowconfigure(i, weight=1, minsize=3)
            row = []
            for j in range(9):
                sudokuSquare = tk.Text(sudokuFrame, bg="white", font=("Helvitica", 20))
                sudokuSquare.tag_configure("centered", justify="center")
                sudokuSquare.tag_add("centered", "1.0", "end")
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

    def solve(self, visual = False):
        # print("Visual:", visual)
        if not self.solver:
            raise AttributeError("Solver not initialized for Visualizer object")

        self.extractText()
        if not self.solver.validGrid(self.grid):
            # print("Unsolvable grid!")
            tk.messagebox.showerror(message="Unsolveable Grid!")
        else:
            solution = []
            self.solving = True
            self.solver.solveSudoku(self.grid, visual=visual)
            self.solving = False
            if not visual:
                self.setAllValues(self.grid)

    def fixValue(self, row, col):
        # print("Fix value called")
        self.buttonGrid[row][col].configure(bg="green")
        self.root.update_idletasks()

    def testValue(self, row, col, value):
        # print("Test Value called")
        self.buttonGrid[row][col].insert("1.0", str(value), "centered")
        self.buttonGrid[row][col].configure(bg="red")
        self.root.update_idletasks()

    def clearValue(self, row, col):
        # print("Clear value called")
        self.buttonGrid[row][col].delete("1.0", tk.END)
        self.buttonGrid[row][col].configure(bg="white")
        self.root.update_idletasks()

    def setAllValues(self, grid):
        for i in range(9):
            for j in range(9):
                self.buttonGrid[i][j].delete("1.0", tk.END)
                self.buttonGrid[i][j].insert("1.0", str(grid[i][j]), "centered")

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.clearValue(i, j)

    def start(self):
        self.root.mainloop()

    def doneSolving(self):
        self.solving = False


