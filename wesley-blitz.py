board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
    ]
isXplayer = True

while True:
    print(board)
    move = input('Put in your move!! as x ,y') # input as x,y, string
    x,y = move.split(",")
    x = int(x)
    y = int(y)
    board[x][y] = "x" if isXplayer else "o"
    isXplayer = not isXplayer
    for row in board:
        if len(set(row)) == 1 and row[0] != "": # wesley goblin, set is math set, no duplicate objects
            exit()
    for row in zip(*board):
        if len(set(row)) == 1 and row[0] != "": # wesley goblin, set is math set, no duplicate objects
            exit()
    if board[0][0] == board[1][1] == board[2][2] != "" :
        exit()
    if board[0][2] == board[1][1] == board[2][0] != "" :
        exit()