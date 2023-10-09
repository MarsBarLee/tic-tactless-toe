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

Removing spaces in board
Before
    Beginning of game
    This is the current board.
    | | | |
    | | | |
    | | | |

    After player move
    This is the current board.
    |X | | |
    | | | |
    | | | |

After
    Beginning of game
    This is the current board.
    | | | |
    | | | |
    | | | |

    After player move
    This is the current board.
    This is the current board.
    |X| | |
    | | | |
    | | | |

Before
def print_board(board):
    print("This is the current board. \n"
    f"|{board[0][0]}|{board[0][1] |{board[0][2]  }| \n"
    ...

After
def print_board(board):
    print("This is the current board. \n"
    f"|{board[0][0] or ' '}|{board[0][1] or ' '}|{board[0][2] or ' '}| \n"
    ...

Achieved by using Truthy or Falsy
                    x   or  y

Truth Table (documentation: https://docs.python.org/3/library/stdtypes.html)
    or|T|F|
    |T|T|F|
    |F|T|F|

T or T = T
    (T) or T = (T)
T or F = T
    (T) or F = (T)
F or T = T
    F or (T) = (T)
F or F = F
    F or (F) = (F)


Logic flow of try and except
Try and except documentation: https://docs.python.org/3/tutorial/errors.html
Before
def get_player_move():
    while True:
        player_move = input("Enter your move: row, column\n")
        try:
            player_move = [int(x) for x in player_move.split(",")]
            return player_move # compare placement of return statement and diff placement effect on loop logic
        except ValueError:
            print("Incorrect move.")

After
def get_player_move():
    while True:
        player_move = input("Enter your move: row, column\n")
        try:
            player_move = [int(x) for x in player_move.split(",")]
        except ValueError:
            print("Incorrect move.")
        return player_move # compare placement of return statement and diff placement effect on loop logic. 
        # bad because line 64 will run line 65 (return player_move) even though it is an incorrect move

---
True, False with itnergers, strings
Using bool()
Why use bool()? Because all built-in types have __bool__ because all built-in types are instances of class of str, int, etc
>>> bool(1)
True
>>> bool(0) 
False
>>> bool(345354) 
True
>>> bool("czxc") 
True
>>> bool("")     
False
>>> x = "foo"
>>> bool(x)
True
---

All built-in types have a bool(""). Because all built-in types have __bool__ because all built-in types are instances of class of str, int, etc


https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

More testing
x = foo
x has multiple built-in functions that we can check with dir()
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> x.capitalize()
'Foo'
>>> z = str()
>>> z
''
>>> z = str("sdfsdf") 
>>> z
'sdfsdf'

Truthy or Falsey with 2 srings
>>> "asdf" or "qwerwerwer"
'asdf'
>>> if (True or False):
...     print("hi")
... 
hi
>>> if "asdf": 
...     print("hi")
... 
hi
>>> if "qwerwerwer":
...     print("hi")
hi
>>> if True or exit():
...     print("hi")
hi
>>> if True or print("!!!"):
...     print("???")
... 
???
>>>
>>> if False or print("!!!"):
...     print("???")
... 
!!! (prints !!! because Truth Table chooses second False obeject if 'False or False')
>>> exit()
---

After
def print_board(board):
    print("This is the current board. \n"
    f"|{board[0][0] or ' '}|{board[0][1] or ' '}|{board[0][2] or ' '}| \n"
    ...

board[0][0] or ' '
board[0][0] = 'X' or 'O' or ''
    Have '' because define board as '' in start_game
        def start_game():
        print(random.choice(quote_repository['start_game']))
        board = [["","",""], ["","", ""], ["","",""]]
    Apply Truth Table to this
    'X' or ' ' = 'X'
        (T) or T = (T)
    'O' or ' ' = 'O'
        (T) or T = (T)
    '' or ' ' = ' '
        F or (T) = (T)
        ergo, a section with ' ', 1 single space

---
Checks for draw() before isWin()
Problem here is game calls draw instead of win
Running updated_board()
This is the current board.
|X|O|X|
|O|X|O|
|O|X| |

isWin() is running.
They say the only thing you can do is keep going. So... keep going?
Enter your move: row, column
2,2
Running updated_board()
This is the current board.
|X|O|X|
|O|X|O|
|O|X|X|

Sometimes things are a dead-end. Like this. And many, many other things of yours.
Welcome. You might not know, but tic-tac-toe is a pretty simple game.
This is the current board.
| | | |
| | | |
| | | |

isWin() is running.
They say the only thing you can do is keep going. So... keep going?
Enter your move: row, column
---

def start_game():
    print(random.choice(quote_repository['start_game']))
    board = [[" "," "," "], [" "," ", " "], [" "," "," "]]
    isXTurn = True
    print_board(board)
    while True: # almighty True
        print(random.choice(quote_repository['ask_player_for_move']))
        player_move = get_player_move()
        while (not is_valid_move(player_move, board)):
            print(random.choice(quote_repository['invalid_move']))
            player_move = get_player_move()
        board = update_board(board, player_move, isXTurn)
        print_board(board)
        if isWin(board):
            print(random.choice(quote_repository['win']))
            break # break so program doesn't run check_draw()
        check_draw(board)
        isXTurn = not isXTurn

