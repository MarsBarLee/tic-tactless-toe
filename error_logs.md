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
Error: "(" was not closed
Reason: 
---

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".\tic-tactless-toe.py", line 44, in get_player_move
    player_move = int(player_move)
ValueError: invalid literal for int() with base 10: '1,2
Reason: Cannot apply int() function to string '1,2' into 1 and 2 intergers.
int() would work on '54' to 54 intereger, but is thrown off by the comma
Solution: To remove the comma, we can use split()
text.split(",")
Result: ['1','2']

List Comprehension: https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/#:~:text=The%20most%20Pythonic%20way%20to,x)%20built%2Din%20function.

split() and list comprehension in one line
text = "1,2"
new_text = [int(x) for x in text.split(",")]
print(new_text)
