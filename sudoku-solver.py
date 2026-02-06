board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# defining a function for finding empty cells
def empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row,col #Returns the row and coloumn of empty cell
    return None #Executes if the board is already full

# Finding valid numbers to choose
def valid(board,num,pos):
    row,col = pos

    #Checking row validity
    for i in range(9):
        if board[row][i]==num:
            return False
    
    #Checking coloumn validity
    for i in range(9):
        if board[i][col]==num:
            return False
    
    #Finding the 3x3 box starting row and coloumn
    box_row = (row//3)*3
    box_col = (col//3)*3

    #Checking 3x3 box validity
    for i in range(box_row,box_row+3):
        for j in range(box_col,box_col+3):
            if board[i][j]==num:
                return False
    
    return True

#Defining the solver function
def solve(board):
    posfind = empty(board)
    if not posfind:
        return True #This part give the row and coloumn as result the board is not full and else true which means the board is solved. Also this is the base call for recursive backtracking.
    else:
        row,col = posfind

    for num in range(1,10):
        if valid(board,num,posfind):
            board[row][col] = num #Trying to solve using this number
            
            if solve(board): #Recursive call
                return True
            
            board[row][col] = 0 #Step for undoing step in case of wrong choice of numbers available

    return False

#Function to display the solved board
def display_board(board):
    for row in board:
        print(row)

#RUNNING PART OF THE PROGRAM
print("The unsolved board:")
display_board(board)
print("\n")

solve(board)

print("The solved board:")
display_board(board)