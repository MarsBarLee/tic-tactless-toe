    print(f"
     '''
     |{[0][0]} |{[0][1]} |{[0][2]} |
     |{[1][0]} |{[1][1]} |{[1][2]} |
     |{[2][0]} |{[2][1]} |{[2][2]} |
    ''' 
    "
SyntaxError: EOL while scanning string literal
String literal is unterminated
Solution: Put in closing quotation mark
---


    def check_win():
    ^
IndentationError: expected an indented block
Reason: The function above it, update_board(). was empty, only has pseudo-code comments.
Soltuion: Add a line to update_board()
---

def check_win():
    # horizontal win condition (3 variations)
    # top row
    if (board[0][0] = 'X' or 'O') & (board[0][1] = 'X' or 'O') & (board[0][2] = 'X' or 'O'):
Error: "(" was not clsoed
Reason: 