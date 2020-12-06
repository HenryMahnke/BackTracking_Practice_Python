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


def solve(bo):

    find = find_empty(bo) # this finds the spot that is 0
    if not find: # if it cant find anything that is empty its solved
        return True  # found solution
    else:
        row, col = find  # set the row = i and the col = j from the find_empty method

    for i in range(1, 10):  # try values 1 through 9
        if valid(bo, i, (row, col)):  # if valid insert num
            bo[row][col] = i  # at x point put in value 1 through 9

            if solve(bo):  # recursively try to solve the board by calling solve on our new board because it has just been modified this works because it will always only have to reset 1 value as it is solving because otherwise the entire board is invalid because of the valid method
                return True

            bo[row][col] = 0  # if we've looped through 1-9 and none of them are valid we return false so we are going to back track to our last number and change that

    return False  # if we looped through all numbers and none of them work if that happens, return false, so back track and reset prior value


def valid(bo, num, pos):  # board, number:inserted and position is position of empty

    # check row
    for i in range(len(bo[0])):  # loops through the cols 0-8
        if bo[pos[0]][i] == num and pos[1] != i:
            # the first part checks through each column in the row and looks to see if it is equal to the number we just added in and if the position is the one we just looked at it and inserted it into the board we skip past that because obviously we just put it in but if there are 2 numbers that are the same then you screwed up man
            return False
    # check column
    for i in range(len(bo)):  # loops through row 0-8
        if bo[i][pos[1]] == num and pos[0] != i:
            # check if current col value is equal to the number we just inserted and make sure not the same position of the thing we just inserted into
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # for example if at pos 0,3 or point 1,4 then say 0/3 is 0 so in highest up box  and 3/3 is 1 so in second box
    for i in range(box_y * 3, box_y * 3 + 3):  # for  in range of between y value 2*3 6th index or 7th number/ 3rd box through 8th index
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):  # row
        if i % 3 == 0 and i != 0:  # this is here so that every three rows it will print the horizontal line
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):  # 9 there are 9 characters in the row
            if j % 3 == 0 and j != 0:  # so there isnt a line printed on the far left just to start
                print(" | ", end="")

            if j == 8:  # if at end of row
                print(bo[i][j])
                # i is rows j is cols so if row 1 2 3 at the column position1-9
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):  # rows
        for j in range(len(bo[0])):  # cols
            if bo[i][j] == 0:
                return (i, j)  # return the row and col

    return None  # if no blank squares return none


print_board(board)
solve(board)
print("-------------------------------")
print_board(board)