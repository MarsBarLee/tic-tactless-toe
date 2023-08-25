# Overarching program

# board = [[" "," ", " "], [" "," ", " "], [" "," ", " "]] # final board
board = [["top left","top middle", "top right"], ["middle left","middle middle", "middle right"], ["bottom left","bottom middle", "bottom right"]]  # testing board, not final values

def print_board():
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

def start():
    # print current board
    print_board()

def update_board(row, column, value):
    print("Running updated_board()")
    print_board() # print current board
    board[row][column] = value
    print_board() # print updated board
    # user side: python -c "from file_name import function;function()"
    # user side: python -c 'import tic-tacless-toe; print tic-tactless-toe.update_board()'
    # python3 -i file_name.py aka python3 -i tic-tactless-toe.py

start()

"""
  - start()
  - check_valid_move()
  - update_board()
  - check_win()
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
            if (board[0][0] = 'X' or 'O') & (board[1][1] = 'X' or 'O') & (board[2][2] = 'X' or 'O') ...
            veritcal win condition 2
               0, 1, 2
            0 |  |o |  |
            1 |  |o |  |
            2 |  |o |  |
            if (board[0][1] = 'X' or 'O') & (board[1][1] = 'X' or 'O') & (board[2][1] = 'X' or 'O') ...
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