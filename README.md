# Sudoku Solver using PYTHON

A Python based sudoku solver that uses *backtracking algorithm* to solve any valid 9x9 sudoku puzzle

---

## Algorithms Used:
- Backtracking
- Recursion
- Constaint Satisfaction

The solver first finds the empty cell in the given unsolved sudoku and tries numbers from 1 to 9 in the founded empty cells, checks sudoku constraints(number not in row, coloumn and the 3x3 box consisting the cell)
Then it uses backtracks when a dead end is reached

---

## Features

- Solves 9x9 sudoku
- Accepts input using a GUI using tkinter module
- Displays result using the same GUI
- Uses recursion with backtracking
- Clean and readable implementation
- Easy to understand

---

## Version History
- **v1.0**- Basic program with just the logic flow which used a pre-initialised sudoku puzzle to demonstrate
- **v2.0**- Added user inputting system for puzzles. Added GUI for inputting unsolved puzzle and showing the solved one.

---

## How to run

Clone the repository:
```bash
git clone
https://github.com/navv8/Sudoku-Solver.git

