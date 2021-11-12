import tkinter as tk

class Visualizer:
    def __init__(self):
        root = tk.Tk()
        root.geometry("500x700")
        buttonFrame = tk.Frame(root, width = 500, height = 200, bg = "blue")
        buttonFrame.pack(side=tk.BOTTOM)
        testButton = tk.Button(buttonFrame, width = 10, height = 5)
        testButton.pack()

        self.grid = []
        sudokuFrame = tk.Frame(root, width = 500, height = 500, bg = "yellow")
        for i in range(9):
            sudokuFrame.columnconfigure(i, weight = 1, minsize = 5)
            sudokuFrame.rowconfigure(i, weight = 1, minsize = 3)
            row = []
            for j in range(9):
                sudokuSquare = tk.Text(sudokuFrame, bg = "green")
                row.append(sudokuSquare)
                sudokuSquare.grid(column = j, row = i)
            self.grid.append(row)
        sudokuFrame.pack()
        root.mainloop()



v = Visualizer()