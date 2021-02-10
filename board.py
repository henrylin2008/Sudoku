board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(board): # print out the board
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:   # print every 3 rows
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):  # every position in row
            if j % 3 == 0 and j != 0:   # on every 3rd element but not first column
                print(" | ", end="")    # end="": don't go to next line

            if j == 8:  # last position in the row
                print(board[i][j])  # draw /n, make sure it goes to the next line
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)