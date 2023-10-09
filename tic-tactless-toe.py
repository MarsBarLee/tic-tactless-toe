# a tic-tac-toe game that insults you at every turn. winning does not guarantee exemption.
import random

def print_board(board):
    print("This is the current board. \n"
    f"|{board[0][0]}|{board[0][1]}|{board[0][2]}| \n"
    f"|{board[1][0]}|{board[1][1]}|{board[1][2]}| \n"
    f"|{board[2][0]}|{board[2][1]}|{board[2][2]}| \n"
    )

def start_game():
    print(random.choice(quote_repository['start_game']))
    board = [[" "," "," "], [" "," ", " "], [" "," "," "]]
    isXTurn = True
    print_board(board)
    while True:
        print(random.choice(quote_repository['ask_player_for_move']))
        player_move = get_player_move()
        while (not is_valid_move(player_move, board)):
            print(random.choice(quote_repository['invalid_move']))
            player_move = get_player_move()
        board = update_board(board, player_move, isXTurn)
        print_board(board)
        if isWin(board):
            print(random.choice(quote_repository['win']))
            break
        if check_draw(board):
            print(random.choice(quote_repository['draw']))
            start_game()
        isXTurn = not isXTurn
        
def get_player_move():
    while True:
        player_move = input("Enter your move: row, column\n")
        try:
            player_move = [int(x) for x in player_move.split(",")]
            return player_move
        except ValueError:
            print("Incorrect move.")
        

def update_board(board, player_move, isXTurn):
    if(isXTurn):
        board[player_move[0]][player_move[1]] = "X"
    else:
        board[player_move[0]][player_move[1]] = "O"
    return board

def is_valid_move(player_move, board):
    row = player_move[0]
    column = player_move[1]
    if not (0<= row <=2 and 0<= column <=2):
        print(random.choice(quote_repository['invalid_move']))
        return False
    if board[row][column] != " ":
        print('That section of the board is taken. Place your move elsewhere.')
        return False
    return True

def isWin(board):
    # horizontal win condition (3 variations)
    # top row
    isWin = False
    if ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == 'X')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == 'O')):
        isWin = True
    # middle row
    elif ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == 'X')) or ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == 'O')):
        isWin = True
    # bottom row
    elif ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == 'X')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == 'O')):
        isWin = True
    # vertical win condition (3 variations)
    # left column
    elif ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == 'X')) or ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == 'O')):
        isWin = True
    # middle column
    elif ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == 'X')) or ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == 'O')):
        isWin = True
    # right column
    elif ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == 'X')) or ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == 'O')):
        isWin = True
    # diagonal win conditions (2 variations)
    # left-to-right diagonal
    elif ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == 'X')) or (board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == 'O'):
        isWin = True 
    # right-to-left diagonal
    elif ((board[0][2] == 'X') and (board[1][1] == 'X') and (board[2][0] == 'X')) or (board[0][2] == 'O') and (board[1][1] == 'O') and (board[2][0] == 'O'):
        isWin = True 
    return isWin

quote_repository = {
    "start_game": [
        "Welcome, I guess. Why you started, I don't even know.",
        "Welcome. I don't need to explain tic-tac-toe to you, do I?",
        "Welcome. You might not know, but tic-tac-toe is a pretty simple game."
    ],
    "ask_player_for_move": [
        "This is the part where you keep trying to not lose."
        "That move didn't totally suck!",
        "They say the only thing you can do is keep going. So... keep going?"
    ],
    "invalid_move": [
        "Hey genius. That's an invalid move.",
        "That's not going to work. Try better.",
        "Do you even know how to play a simple game like tic-tac-toe?"
    ],
    "win": [
        "Hey, everybody, get a load of this guy here, they won!",
        "Hey, not bad, for once.",
        "Winning can be fun, once you get the hang of it.",
        "You've won. I'm not sure why you kept going, but it worked out in the end."
    ],
    "draw": [
        "Despite not being very good, at least you stuck through it to the very end.",
        "Sometimes things are a dead-end. Like this. And many, many other things of yours.",
        "You really are playing at the edge of your abilities."
    ],
    "restart": [
        "Yeah, you didn't play great. Might as well try again (but I don't know what would be different).",
        "If first you don't succeed... restart many more times.",
        "Yeah, let's pretend that last play didn't happen."
    ],
    "quit": [
        "You weren't getting anywhere close to winning anyway.",
        "At least you're aware that you're not that good.",
        "Come back when you're more... capable."
    ]
}

def check_draw(board):
    filled_section_counter = 0
    for row in board:
        for column in row:
            if column != " ":
                filled_section_counter += 1
                if filled_section_counter == 9:
                    return True
    return False

def restart():
    # when the player input the restart command
    print(random.choice(quote_repository['restart']))
    start_game()

def quit_game():
    # when the player input the quit command
    print(random.choice(quote_repository['quit']))
    # print('You have chosen to quit the game. The game will now quit.')
    quit()

def test_suite():
    # X win
    # horizontal win
    assert(isWin([["X","X","X"], ["","", ""], ["","",""]]))
    assert(isWin([["","",""], ["X","X", "X"], ["","",""]]))
    assert(isWin([["","",""], ["","", ""], ["X","X","X"]]))   
    # vertical win
    assert(isWin([["X","",""], ["X","", ""], ["X","",""]]))
    assert(isWin([["","X",""], ["","X", ""], ["","X",""]]))
    assert(isWin([["","","X"], ["","", "X"], ["","","X"]]))
    # diagonal win
    assert(isWin([["X","",""], ["","X", ""], ["","","X"]]))
    assert(isWin([["","","X"], ["","X", ""], ["X","",""]]))
    # O win
    # horizontal win
    assert(isWin([["O","O","O"], ["","", ""], ["","",""]]))
    assert(isWin([["","",""], ["O","O","O"], ["","",""]]))
    assert(isWin([["","",""], ["","", ""], ["O","O","O"]]))   
    # vertical win
    assert(isWin([["O","",""], ["O","", ""], ["O","",""]]))
    assert(isWin([["","O",""], ["","O", ""], ["","O",""]]))
    assert(isWin([["","","O"], ["","", "O"], ["","","O"]]))
    # diagonal win
    assert(isWin([["O","",""], ["","O", ""], ["","","O"]]))
    assert(isWin([["","","O"], ["","O", ""], ["O","",""]]))
    # not winning board = True
    assert(not isWin([["","O",""], ["X","O", ""], ["O","",""]]))
    # draw
    assert(check_draw([["X","O","O"], ["X","O", "X"], ["O","X","O"]]))

start_game()
# isWin([["X","",""], ["X","", ""], ["X","",""]]) 
# test_suite()