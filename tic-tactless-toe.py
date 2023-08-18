# Overarching program
def tic-tactless-toe() {
    # Data structure: 2D array
    # data_structure = [[c1,c2,c3], [c1,c2,c3], [c1,c2,c3]]
    data_structure = [[0,0,0], [0,0,0], [0,0,0]]
    # value of section is 0,1, or 2. Default state is blank: 0. X is 1. O is 2.
    # Input function
    # Store player turn
    # Ask player to make a move
    # Show state of game in terminal
    # Check if valid move
        # if not, reject and ask player to try again
    # Change state of game by taking player input and updating data strcuture
    # Update game in terminal
    # Win logic
    # Draw logic
    # Quit logic
}

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