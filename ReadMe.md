Personal sudoku solver project with backtracking. I did not follow any tutorials for this project. Made using the Tkinter library in Python.

**Step 1:**

Enter the digits of a given sudoku into the grid

![step1](https://user-images.githubusercontent.com/70418659/143286700-812dd9f7-b3e2-46ff-92c4-6fba29b6ea9d.png)

**Step 2a:**

If you just want the answers as fast as possible, clicking the [Solve] button will quickly fill the missing digits with backtracking

![step2](https://user-images.githubusercontent.com/70418659/143286873-d8682451-5d6f-4034-a954-e8fbebaf1fa5.png)

**Step 2b:**

To visualize how the backtracking algorithm works, clicking the [Visualize] button will fill in the digits more slowly, showing them as red when the algorithm is testing possibilities, and green when the algorithm determines that the digit is completely valid.

![step3](https://user-images.githubusercontent.com/70418659/143287086-4175f4ca-0aad-4cfa-bf3b-e8cafa555983.PNG)

![step4](https://user-images.githubusercontent.com/70418659/143287104-2c4b4642-a294-4234-8117-4f907bcfac87.png)

**Step 3:**

Clicking the [Reset] button will reset the grid to a blank slate.

Todo list:

_ Handle long runtimes

_ More efficient algorithm (fixes previous step?)

_ Fix visualization freezing (threading?)

_ Keep pre-entered digits on screen after resetting

- Option to load sudoku from file
