# Overarching program
# TODO: For Mars to do, translation dictionary of row, column to array values
# TODO make player_move be an array
# board = [[" "," ", " "], [" "," ", " "], [" "," ", " "]] # final board
import random

def print_board(board):
    # print(board[0][0]) # only print value
    print(f"Here is the top left section's value: {board[0][0]}") # with string literal
    # hardcoded example
    # '''
    # |{[0][0]} |{[0][1]} |{[0][2]} |
    # |{[1][0]} |{[1][1]} |{[1][2]} |
    # |{[2][0]} |{[2][1]} |{[2][2]} |
    #''' 
    #)
    print("This is the current board. \n"
    f"|{board[0][0]} |{board[0][1]} |{board[0][2]} | \n"
    f"|{board[1][0]} |{board[1][1]} |{board[1][2]} | \n"
    f"|{board[2][0]} |{board[2][1]} |{board[2][2]} | \n"
    )

def start_game():
    print(random.choice(quote_repository['start_game']))
    board = [["","",""], ["","", ""], ["","",""]]
    isXTurn = True
    # print current board
    print_board(board)
    while (not isWin(board)):
        print(random.choice(quote_repository['ask_player_for_move']))
        player_move = get_player_move()
        while (not is_valid_move(player_move)):
            print(random.choice(quote_repository['invalid_move']))
            player_move = get_player_move()
        board = update_board(board, player_move, isXTurn)
        print_board(board)
        isXTurn = not isXTurn
        
def get_player_move():
    # print("Enter your move: row, column\n")
    # TODO: For Mars to do, translation dictionary of row, column to array values
    player_move = input("Enter your move: row, column\n")
    # TODO make player_move be an array, eg player_move = [2,2] aka bottom right, because input returns a string
    # player_move is used in update_board(), board[player_move[0]][player_move[1]] = "X"
    print(f"This the variable player_move: {player_move}")
    print(f"This the data type of player_move: {type(player_move)}")
    player_move = [int(x) for x in player_move.split(",")]
    print(f"This the variable player_move after int(): {player_move}")
    print(f"This the data type of player_move after int(): {type(player_move)}")
    return player_move

def update_board(board, player_move, isXTurn):
    print("Running updated_board()")
    # print_board() print current board, for testing, remove later
    if(isXTurn):
        board[player_move[0]][player_move[1]] = "X"
    else:
        board[player_move[0]][player_move[1]] = "O"
    return board
    # user side: python -c "from file_name import function;function()"
    # user side: python -c 'import tic-tacless-toe; print tic-tactless-toe.update_board()'
    # python3 -i file_name.py aka python3 -i tic-tactless-toe.py

def is_valid_move(player_move):
    row = player_move[0]
    column = player_move[1]
    # needs to take input from update_board()
    # check if in bound of board[row][column], board[0-2][0-2]
    if 0<= row <=2 and 0<= column <=2:
        print('Valid move. Updating the board.')
        return True
        # let rest of update_function() run... move check_valued_move() to update_function()? But want to keep modular
        # attempt: in update_board(), if valid_move = true, run this section of update_board()...
    else:
        print(random.choice(quote_repository['invalid_move']))
        # print('Invalid move! Put in your moves, with the correct values.')
        return False
        # stop the function from running further

def isWin(board):
    # TODO Fix logic in here. Problem: Doesn't need to be XXX to win, with current logic could be XOX 
    print("isWin() is running.")
    # horizontal win condition (3 variations)
    # top row
    isWin = False
    if ((board[0][0] == 'X') and (board[0][1] == 'X') and (board[0][2] == 'X')) or ((board[0][0] == 'O') and (board[0][1] == 'O') and (board[0][2] == 'O')):
        # game_status = 'win_game'
        print('Congratulations! You won! Horizontal win, top row.')
        isWin = True
    # middle row
    elif ((board[1][0] == 'X') and (board[1][1] == 'X') and (board[1][2] == 'X')) or ((board[1][0] == 'O') and (board[1][1] == 'O') and (board[1][2] == 'O')):
        game_status = 'win_game'
        print('Congratulations! You won! Horizontal win, middle row.')
        isWin = True
    # bottom row
    elif ((board[2][0] == 'X') and (board[2][1] == 'X') and (board[2][2] == 'X')) or ((board[2][0] == 'O') and (board[2][1] == 'O') and (board[2][2] == 'O')):
        game_status = 'win_game'
        print('Congratulations! You won! Horizontal win, bottom row.')
    # vertical win condition (3 variations)
    # left column
    elif ((board[0][0] == 'X') and (board[1][0] == 'X') and (board[2][0] == 'X')) or ((board[0][0] == 'O') and (board[1][0] == 'O') and (board[2][0] == 'O')):
        game_status = 'win_game'
        print('Congratulations! You won! Vertical win, left column.')
        isWin = True
    # middle column
    elif ((board[0][1] == 'X') and (board[1][1] == 'X') and (board[2][1] == 'X')) or ((board[0][1] == 'O') and (board[1][1] == 'O') and (board[2][1] == 'O')):
        game_status = 'win_game'
        print('Congratulations! You won! Vertical win, middle column.')
        isWin = True
    # right column
    elif ((board[0][2] == 'X') and (board[1][2] == 'X') and (board[2][2] == 'X')) or ((board[0][2] == 'O') and (board[1][2] == 'O') and (board[2][2] == 'O')):
        game_status = 'win_game'
        print('Congratulations! You won! Vertical win, right column.')
        isWin = True
    # diagonal win conditions (2 variations)
    # left-to-right diagonal
    elif ((board[0][0] == 'X') and (board[1][1] == 'X') and (board[2][2] == 'X')) or (board[0][0] == 'O') and (board[1][1] == 'O') and (board[2][2] == 'O'):
        game_status = 'win_game'
        print('Congratulations! You won! Diagonal win, left-to-right.')
        isWin = True 
    # right-to-left diagonal
    elif ((board[0][2] == 'X') and (board[1][1] == 'X') and (board[2][0] == 'X')) or (board[0][2] == 'O') and (board[1][1] == 'O') and (board[2][0] == 'O'):
        game_status = 'win_game'
        print('Congratulations! You won! Diagonal win, right-to-left')
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
    "win_game": [
        "Hey, everybody, get a load of this guy here, they won!",
        "Hey, not bad, for once.",
        "Winning can be fun, once you get the hang of it.",
        "I'm not sure why you kept going, but it worked out in the end."
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

filled_section_counter = 0

def check_draw():
    for row in board:
        for column in row:
            if column != " ":
                print('Filled section, increase filled_section_counter by one') # remove in final
                filled_section_counter += 1
                if filled_section_counter == 9:
                    game_status = 'draw'
                    print('The game has come to a draw.')
                    # restart_game prompt?
            else:
                print('Empty section') # remove in final
                # nothing happens

def restart():
    # when the player input the restart command
    game_status = 'restart'
    print('You have chosen to restart the game. The game will now restart.')
    board = [["top left","top middle", "top right"], ["middle left","middle middle", "middle right"], ["bottom left","bottom middle", "bottom right"]]  # testing board, not final values
    # when game has reached a win
    game_status = 'restart'
    print('A player has won. The game will now restart.') # change to X/Y player has won
    board = [["top left","top middle", "top right"], ["middle left","middle middle", "middle right"], ["bottom left","bottom middle", "bottom right"]]  # testing board, not final values
    # when game has reached a down
    game_status = 'restart'
    print('There is a draw. Nobody wins! The game will now restart.') # change to X/Y player has won
    board = [["top left","top middle", "top right"], ["middle left","middle middle", "middle right"], ["bottom left","bottom middle", "bottom right"]]  # testing board, not final values

def quit_game():
    # when the player input the quit command
    game_status = 'quit'
    print('You have chosen to quit the game. The game will now quit.')
    quit()

def test_suite():
    # X win
    # horizontal win
    isWin([["X","X","X"], ["","", ""], ["","",""]])
    isWin([["","",""], ["X","X", "X"], ["","",""]])
    isWin([["","",""], ["","", ""], ["X","X","X"]])    
    # vertical win
    isWin([["X","",""], ["X","", ""], ["X","",""]])
    isWin([["","X",""], ["","X", ""], ["","X",""]])
    isWin([["","","X"], ["","", "X"], ["","","X"]])
    # diagonal win
    isWin([["X","",""], ["","X", ""], ["","","X"]])
    isWin([["","","X"], ["","X", ""], ["X","",""]])
    # O win
    # horizontal win
    isWin([["O","O","O"], ["","", ""], ["","",""]])
    isWin([["","",""], ["O","O","O"], ["","",""]])
    isWin([["","",""], ["","", ""], ["O","O","O"]])    
    # vertical win
    isWin([["O","",""], ["O","", ""], ["O","",""]])
    isWin([["","O",""], ["","O", ""], ["","O",""]])
    isWin([["","","O"], ["","", "O"], ["","","O"]])
    # diagonal win
    isWin([["O","",""], ["","O", ""], ["","","O"]])
    isWin([["","","O"], ["","O", ""], ["O","",""]])

start_game()
# isWin([["X","",""], ["X","", ""], ["X","",""]]) 
# test_suite()


"""
  - start()
  - is_valid_move()
  - update_board()
  - isWin()
  - check_draw()
  - restart()
  - quit()
  - switch_players_turn()
  - print_board()
"""

"""
def tic_tactless_toe():
    Data structure: 2D array
        board = [[c1,c2,c3], [c1,c2,c3], [c1,c2,c3]] # as rows and columns
        board = [[0,0,0], [0,0,0], [0,0,0]] # as intergers
        board = [[" "," ", " "], [" "," ", " "], [" "," ", " "]] # as  strings
        value of section of board is 0, 1, or 2. Default state is blank: 0. X is 1. O is 2.
        store value of board as intergers instead of strings because... more optimized? will be converted to string to player? needless changing?
    Input function
        Change value of nestled array, of r1,c1 to 1
        board[0,0] = [1]
    Ask player to make a move
        X Player changes value of nestled array, of r1,c1 to 1
        X player's input: r1,c1,1
        Take in answer in 3 parts 'r1', 'c1', '1', remove commas
        change r1=0, r2=1, r3=2
        change c1=0, r2=1, c2=2
        r1,c1,1 = 0,0,1
        therefore, r1,c1,1 should run the function board[0,0] = [1]
    Store player's move
        X_player_move: r1,c1,1 aka 0,0,1
        def update_board(row, column, value)
        update_board(0, 0, 1)
    Show state of game in terminal
        long print function over multiple lines? using \n
        taking the value of 
             c1,    c2,    c3
        r1 |[0][0]|[0][1]|[0][2]|
        r2 |[1][0]|[1][1]|[1][2]|
        r3 |[2][0]|[2][1]|[2][2]|
        printing one row as
            print(f"|{[0][0]} |{[0][1]} |{[0][2]} |")
        printing over multiple rows
            print(f
            '''
            |{[0][0]} |{[0][1]} |{[0][2]} |
            |{[1][0]} |{[1][1]} |{[1][2]} |
            |{[2][0]} |{[2][1]} |{[2][2]} |
            '''
            )
        Translate value of '0' into blank: some sort of translation? 
            pass through... a dictionary? maybe not print yet, but translate through dictionary and then print the dictionary results? so write a translation dictionary and a function that runs the translation? 
            don't print the board directly, store the value of the board
            example of key-value pairs
                0: ' '
                1: 'X'
                2: 'O'
            Use the translation() and str.maketrans() methods
                translation_dict = {0:" ", 1:"X", 2:"O"}
                board = "|{[0][0]} |{[0][1]} |{[0][2]} |"
                    note: do we need to convert interger values into strings? Using the .int method in_between...?
                create a translation table using the dictionary
                    translation_table = str.maketrans(translation_dict)
                translate the string using the table
                    board_as_x_o = board.translate(translation_table)
    Check if valid move
        if not, reject and ask player to try again
        x_player_move = r1,c1,1
        Use translation dictionary again, but
        row_column_translate_dict = {"r1":"0", r2":"1", r1":"2", "c1":"0", c2":"1", c1":"2"}
        if x_player_move != between 0 and 2, reject answer
        once again, seems like a lot of shuffling between integer
    Change state of game by taking player input and updating data strcuture
        X_player_move: r1,c1,1 aka 0,0,1
        def update_board(row, column, value)
        update_board(0, 0, 1)
    Update game in terminal
        Take from above 'Show state of game in terminal'
    Switch players
        Boolean logic? eg x_player is 0, o_player is 1. Or is it x_player's turn? True, False. If x_player turn False, turn o_player's to True
    Win logic
        example of player x winning board
            c1,c2,c3
        r1 |x |  |o |
        r2 |  |x |o |
        r3 |o |o |x |
        Behind the scenes...
        if (winning condition), then (run win function)
        winning condition is r1c1, r2,c2, r3,c3 aka board = [["X"," ", "o"], [" ","X", "o"], ["o","o", "X"]]
        wiinning conditions
            horizontal (3 variations), vertical (3 variations), diagonal (2 variations)
            for either player x or o
            do i need to hardcode each win condition? and what about the other sections of the boards where it doesn't matter of blank or opponent's section?
            diagonal win variation 1
                0, 1, 2
            0 |x |  |  |
            1 |  |x |  |
            2 |  |  |x |
            if (board[0][0] = 'X') and (board[1][1] = 'X') and (board[2][2] = 'X') ...
            veritcal win condition 2
               0, 1, 2
            0 |  |o |  |
            1 |  |o |  |
            2 |  |o |  |
            if (board[0][1] = 'X') and (board[1][1] = 'X') and (board[2][1] = 'X') ...
    Draw logic
        When all sections of board are filled up without any win conditions
        Filled up: If all section is not " ". Check for all using for loop?
        for row in board
            for column in row
                if column != " "
                if all columns are not != " "... if != " " 3 times, that's a filled row. if filled row happens 3 times, than make a draw
                if filled_section_counter = 3
                    filled_row_counter += 1
                if filled_row_counter = 3
                    draw_game()
    Restart logic
        if player inputs "restart" as their answer, clear board, reset player
    2 players or play against computer mode
        Future feature
    Tactless quote
        A repository of quotes, depending on conditions
        Conditions: New game, next move, restart, 2 player win/lose, draw
        For each condition, minimum of 3 quotes
        Data structure: object? with each condition and quortes being key-value pairs
    """

"""
Terminal view of board
    c1,c2,c3
r1 |x |  |o |
r2 |  |  |o |
r3 |o |o |x |

Asking player's input
Player X
"What's your next big brain move, egghead?"
Input your answer as rows and columns eg
r2,c2
to add your X to the middle of the board

Example of player input
r2,c2

Updated terminal view of board
    c1,c2,c3
r1 |x |  |o |
r2 |  |x |o |
r3 |o |o |x |

Winning message
"Hey, you actually won. Maybe you do know something about tic_tac_toe."
Reset game? Input as y or n
y

New game
"Hey dingus, let's play tic_tac_toe. Or rather, tic_tactless_toe. You can probably guess whose the tactless one."
Player O
"What's your next big brain move, egghead?"
Input your answer as rows and columns eg
r2,c2
to add your O to the middle of the board

    c1,c2,c3
r1 |  |  |  |
r2 |  |  |  |
r3 |  |  |  |
"""