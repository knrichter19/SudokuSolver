import tkinter as tk

class Visualizer:
    def __init__(self):
        root = tk.Tk()
        #root.geometry("500x700")
        buttonFrame = tk.Frame(root, width = 500, height = 200)
        buttonFrame.pack(side=tk.BOTTOM)

        sudokuFrame = tk.Frame(root, width = 500, height = 500)
        sudokuFrame.pack()


        testButton = tk.Button(buttonFrame, width = 10, height = 5)
        testButton.pack()
        self.grid = []

        for i in range(9):
            row = []
            for j in range(9):
                sudokuSquare = tk.Entry(sudokuFrame, bg = "green", width = 2)
                row.append(sudokuSquare)
                sudokuSquare.grid(column = j, row = i)
            self.grid.append(row)
        root.mainloop()



v = Visualizer()