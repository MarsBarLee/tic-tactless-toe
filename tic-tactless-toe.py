# Overarching program
def tic-tactless-toe():
    # Data structure: 2D array
    # board = [[c1,c2,c3], [c1,c2,c3], [c1,c2,c3]]
    board = [[0,0,0], [0,0,0], [0,0,0]]
    # value of section of board i`s 0,v 1, or 2. Default state is blank: 0. X is 1. O is 2.
    # Input function
        # Change value of nestled array, of r1,c1 to 1
        # board[0,0] = [1]
    # Store player turn
        # X Player changes value of nestled array, of r1,c1 to 1
        # X player's input: r1,c1,1
        # Take in answer in 3 parts 'r1', 'c1', '1', remove commas
        # change r1=0, r2=1, r3=2
        # change c1=0, r2=1, c2=2
        # r1,c1,1 = 0,0,1
        # therefore, r1,c1,1 should run the function board[0,0] = [1]
    # Ask player to make a move
    # Show state of game in terminal
    # Check if valid move
        # if not, reject and ask player to try again
    # Change state of game by taking player input and updating data strcuture
    # Update game in terminal
    # Win logic
    # Draw logic
    # Quit logic

"""
Terminal view of board
    c1,c2,c3
r1 |x |  |o |
r2 |  |  |o |
r3 |o |o |x |

Aking player's input
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
"Hey, you actually won. Maybe you do know something about tic-tac-toe."
Reset game? Input as y or n
y

New game
"Hey dingus, let's play tic-tac-toe. Or rather, tic-tactless-toe. You can probably guess whose the tactless one."
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