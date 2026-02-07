import tkinter as tk
from tkinter import messagebox as msg
from solver import solve,valid

#Creating a tkinter window
root = tk.Tk()
root.title("SUDOKU SOLVER")
root.resizable(False, False)

#Defining the cells of the Sudoku board
cells= {}
for row in range(9):
    for col in range(9):
        
        #Adding different bg colours for sudoku 3x3 grids and also defining properties of each cell
        box_row= row//3
        box_col = col//3
        if (box_row == box_col or (box_row == 0 and box_col == 2) or (box_row==2 and box_col==0)):#Condition for different colours for different #x3 boxes
            entry = tk.Entry(root, width=2, font=("Arial",18), justify="center", bd=2,bg="#fbfbfb")
        else:
            entry = tk.Entry(root, width=2, font=("Arial",18), justify="center", bd=2,bg="#b5b5b5")

        entry.grid(row = row, column=col,)
        cells[(row,col)]=entry

#Defining the function to take input in the shown sudoku board from the user.It also validates the data entered
def read():
    board = []

    #Reading the values
    for row in range(9):
        current_row = []
        for col in range (9):
            value = cells[(row,col)].get()

            #Validation of data
            if value == "":
                current_row.append(0)
            elif value.isdigit() and 1 <= int(value) <=9:
                current_row.append(int(value))
            else:
                msg.showerror("INVALID INPUT\n",f"Invalid value at the position ({row+1}, {col+1})")
                return None
        
        board.append(current_row)
    
    return board

#Defining a function to clear each cell, insert solved number and lock all cells after clicking solve button
def board_fill(board):
    for row in range(9):
        for col in range(9):
            cell = cells[(row,col)]
            cell.delete(0,tk.END)# Clears whatever typed in the cell
            cell.insert(0, board[row][col])# Inserts the solved number
            cell.config(state="readonly")# Locks the cell after pressing SOLVE button

#Defining a function with similar functionality of valid() in solver file to avoid TypeError during gui validation occuring because valid() has 3 arguments
def gui_valid(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                if not valid(board, num, (row,col)):
                    board [row][col] = num
                    return False
                board[row][col] = num
    return True


#Defining a function to connect gui and program logic solver file
def connect():

    status.config(text="Solving...")# For showing the label

    board = read()# Reading board from gui

    if board is None:
        return # Nothing is returned as the msg is already shown during validation part of read() function
    
    #Showing error message if the entered sudoku is invalid using the cloned function(Validation before solving)
    if not gui_valid(board):
        msg.showerror("INVALID SUDOKU", "The entered Sudoku is not valid")
        return
    
    solve_button.config(state="normal")# Changing the button configuration

    #Showing messages after solving the board
    if solve(board):
        board_fill(board)
        msg.showinfo("SUCCESS","Sudoku solved successfully")
    else:
        msg.showerror("NO SOLUTION","This Sudoku has no solution")

    status.config(text = "Solved")
    solve_button.config(state="normal")


#Adding a button for the user to initialize solving
solve_button = tk.Button(root, text="SOLVE", font=("Impact, 18"), width ="5", command= connect, justify="center" )
solve_button.grid(row = 9, column=0, columnspan = 9, pady = 10, padx=10)

#Adding a label to show status of solving
status = tk.Label(root, text= "", font=("Arial", 12), fg="#d0f4f4")
status.grid(row = 10, column = 0, columnspan=9)

root.mainloop()
