board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bor):  # print out the board
    for i in range(len(bor)):
        if i % 3 == 0 and i != 0:  # every 3 rows, print ------
            print("- - - - - - - - - - - -")

        for j in range(len(bor[0])):  # every position in row
            if j % 3 == 0 and j != 0:  # on every 3rd element but not first column
                print(" | ", end="")  # end="": don't go to next line

            if j == 8:  # last position in the row
                print(bor[i][j])  # draw /n, make sure it goes to the next line
            else:
                print(str(bor[i][j]) + " ", end="")


# print_board(board)


def find_empty(bor):  # find empty space
    for i in range(len(bor)):
        for j in range(len(bor[0])):  # len of each row
            if bor[i][j] == 0:        # if the space is 0
                return (i, j)           # tuple: (row, col)

    return None     # if no square == 0


# find_empty(board)

def valid(bor, num, pos):
    # check if the board is valid
    # bor: board;
    # num: num inserted into;
    # pos: position to be inserted

    # Check row
    for i in range(len(bor[0])):    # every single column: 0-8
        # bor[0]: first row
        if bor[pos[0]][i] == num and pos[1] != i:   # if duplicate/same number in the row but not current position
            # bor[pos[0]][i] == num: each element in the row == the number just added in
            # pos[1] != i: the position the number just inserted into, then ignore; check rest positions on the row
            return False

    # check Column
    for i in range(len(bor)):   # every single row: 0-8
        if bor[i][pos[1]] == num and pos[0] != i:   # if duplicate/same number in the column and not current position
            # bor[i][pos[1]] == num: every element in the column == the number just inserted in
            # pos[0] != i: not the position; check other positions
            return False

    # check 3x3 (9) box, which box
    # 00 | 01 | 02
    # 10 | 11 | 12
    # 20 | 21 | 22
    box_x = pos[1] // 3    # column; x position: 0, 1, 2
    box_y = pos[0] // 3    # row; y position: 0, 1, 2
    # loop through every 3x3 box
    for i in range(box_y*3, box_y*3 + 3):
        # box_y*3: the result of box_y is 0,1,2, for box on the far right, x3 will give the index position: 6,7,8
        # +3: will wrap around the index to next row, but for loop does not go beyond last item in the row
        for j in range(box_x*3, box_x*3 + 3):
            if bor[i][j] == num and (i, j) != pos:  # if duplicate number in the 3x3 box
                # bor[i][j] == num: if any number in the 3x3 box == number just inserted in
                # (i, j) != pos: skip the position the number just inserted in
                return False

    return True


def solve(bor):
    # use backtrack, recursive
    # base case: the board is full, solution is found

    # base case
    find = find_empty(bor)
    if not find:
        # the solution is found
        return True
    else:
        row, col = find

    for i in range(1, 10):              # loop through values 1 to 9
        if valid(bor, i, (row, col)):   # check if inserted number is a valid solution
            bor[row][col] = i           # if valid, add the number to the board

            if solve(bor):              # recursively try finish the solution by calling the solve function
                return True

            bor[row][col] = 0           # backtrack; reset last element to a different value

    return False


# print_board(board)
# solve(board)
# print("___________________")
# print_board(board)
