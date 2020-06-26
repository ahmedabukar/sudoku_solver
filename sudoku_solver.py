# Sudoku_solver.py  Solves sudoku puzzles uzing backtracking algorithm

# Example sudoku problem
example = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
           [6, 8, 0, 0, 7, 0, 0, 9, 0],
           [1, 9, 0, 0, 0, 4, 5, 0, 0],
           [8, 2, 0, 1, 0, 0, 0, 4, 0],
           [0, 0, 4, 6, 0, 2, 9, 0, 0],
           [0, 5, 0, 0, 0, 3, 0, 2, 8],
           [0, 0, 9, 3, 0, 0, 0, 7, 4],
           [0, 4, 0, 0, 5, 0, 0, 3, 6],
           [7, 0 ,3, 0, 1, 8, 0, 0, 0]]

# Example solution 
solution = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6 ,3, 4, 1, 8, 2, 5, 9]]

def solve (board):
    """Solves sudoku board using backtracking algorithm"""
    if not find_empty(board): 
        return True
    else:
        x, y = find_empty(board)

    for i in range(1, 10):
        if possible (board, i, (x, y)):
            board[x][y] = i

            if solve(board):
                return True

            board[x][y] = 0

    return False
            

def possible (board, val, pos):
    """Checks whether a value is possible"""
    # Check rows
    for i in range(len(board[0])):
        if board[pos[0]][i] == val and pos[1] != i:
            return False

    # Check columns
    for i in range(len(board)):
        if board[i][pos[1]] == val and pos[0] != i:
            return False

    # Finds which 3x3 box the square is in
    x0 = (pos[1] // 3)
    y0 = (pos[0] // 3)

    # Check boxes
    for i in range(y0 * 3, y0 * 3 + 3):
        for j in range(x0 * 3, x0 * 3 + 3):
            if board[i][j] == val and (i, j) != pos:
                return False

    return True

def find_empty (board):
    """Find empty spaces in the sudoku board"""
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def text(board):
    """Represents a sudoku board in text form"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
               print ("| ", end="")
            if (j == 8):
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

text(example)
solve(example)

print("**********************")
text(example)
