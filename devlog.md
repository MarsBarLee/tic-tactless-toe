a tic-tac-toe game that insults you at every turn. winning does not guarantee exemption.

2023-08-18

- 5m: Plan on paper
- 5m: Look up 2D array data structure at https://www.scaler.com/topics/2d-array-in-python/
- 5m: Add comments and pseudocode
- 5m: Add data structure
- 5m: Add terminal view
- 5m: Add asking for player's input
- 5m: Add winning message
- 5m: Add new game section
- 5m: Update data structure and comments
- 10m: Add logic how player's input leads to game logic
- 10m: Write pseudo-code for player's move

2023-08-19

- 5m: Convert terminal view into 2D array logic
- 5m: Add print function for terminal view
- 5m: Add logic for translating values into Xs and Os. Learn ''' to print multiple lines without using \n
- 5m: Look up 'how to translate dictionary python' and the resource https://www.tutorialspoint.com/How-to-translate-a-python-string-according-a-given-dictionary. Learn translate() and str.maketrans() functions
- 5m: Add translation dictionary for terminal view of board
- 5m: Add int() function
- 5m: Add translation dictionary for player's move
- 5m: Reconsider stored value as integers vs strings
- 5m: Add Boolean to switching players logic 
- 5m: Translate winning conditions into board logic
- 5m: Add diagonal win condition logic
- 5m: Add vertical win logic
- 5m: Add draw logic
- 5m: Consider implementing counter manually or with enumerate()
- 5m: Add section and row counter in draw logic for loop
- 5m: Add tactless quote logic
- 5m: Create and fill in infrastructure_overview.md
- 5m: Add functions and data structures to infrastructure_overview.md
- 5m: Add varibles to infrastructure_overview.md
- 5m: Re-arrange tic-tactless-toe.py based on infastructure_overview.md
- 5m: Add print_board() and learn to run .py file locally

2023-08-24

- 5m: Start building a non-hardcoded print_board()
- 5m: Update board with test values and retrieve test value
- 5m: Add a test to print_board() using f-strings to print variable in strings
- 5m: Move placement of quotes and double quotes in multi-line f-string in print_board()
- 5m: Reformat multi-line f-string with f in front of each line and \n at end
- Milestone: print_board() now prints actual value of board variable
- 5m: Add update_board()
- 5m: Learn how to run a function from the command line in a .py file using -c command
- 5m: Try running a function from the command line
- 5m: Learn how to create interactive .py file using python3 command
- 5m: Learn about import vs run_module() 
- 5m: Test out interactive session with 'python3 -i tic-tactless-toe.py' and exit()
- 5m: Test out interactive session with update_board() and print_board()

2023-08-25
- 15m: Talk to Patrick on feedback such has persistent board after exit(), use while loop to consistently ask for next player's move by checking for check_win() and making final version of functions modular

2023-08-28
- Goal: Make functions like update_board() and print_board() modular
- 5m: Add check_valid_move()
- 5m: Add statement to check range of player's values in check_valid_move()
- 5m: Add else statemnet to check_valid_move()
- 5m: Add switch_player_turn()
- 5m: Split start() into start_game() and start_turn()
- 5m: Add check_win()
- 5m: Add diagonal (left-to-right) and horizontal (top row) win conditions to check_win()
- 5m: Add horizontal (middle row), horizontal (bottom row) and vertical win (left column) to check_win()
- 5m: Add vertical (left, right, middle columns) and diagonal (right-to-left) to check_win()
- 5m: Add check_draw()
- 5m: Add restart()
- Thought: Might need to start branching soon since I've laid down most of the most logic and will need to majorly re-arrange things soon eg making functions modular and replacing test values with final values
- 5m: Change quit() into quit_game() to not trigger built-in Python command quit()
- Next-up: Add quote repository as Python class with 'Game states' as key-value pairs, add translation table

2023-08-29
- 5m: Add class for quote_repository
- 5m: Add win_game, draw, restart and quit for quote_repository
- 5m: Add invalid_move, ask_player_for_move adn start_game for quote_repository
- 5m: Add global variable game_status and create an object instance of quote_repository class\
- Next-up: Add 'Game states' to functions, add translation table

2023-08-31
- 5m: Add game_state to various functions
- 5m: Add more game_state to various functions
- Next-up: Test out interactive session with update_board() and print_board() still works
- 10m: Debug errors from interactive session and update error_log.md
- 5m: Debug error ""(" was not closed" in check_win()'
- 5m: Create and switch to debug_check_win() branch

2023-09-01
- 5m: Remove error by replacing if statement with placeholder values
- 5m: Add back OR statement and debug bracket and : errors
- 5m: Run check_win() without errors
- 5m: Use placeholder in starting board to trigger a check_win() condition
- 5m: Read about comparing one variable with multiple possible values at https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-for-equality-against-a-single-value
- Thought: Maybe in future branch, re-implment check_win() with a containment test against a set, eg if 'X' in {board[0][0], board[0][1], board[0][2]}:
- 5m: Re-add and upate rest of win conditions to correct syntax to check_win and run without errors
- 15m: Push debug_check_win() branch, create a PR that summarizes problem and soltuions, merge PR so that debug_check_win commmits are in main branch, create a PR template.

2023-09-02
- 5m: Make add_mermaid_js branch
- 5m: Draw infastructure diagram
- 5m: Draw infastructure diagram with check_win()
- 5m: Move forward with 10 minute draft of infastructure diagram, npm install mermaid
- 5m: Start turning drawn infastructure diagarm into mermaid.js diagram using mermaid.live
- 5m: Download mermaid.js diagram and add .mermaid file
- 5m: Add switch_player_turn to mermaid.js diagram
- Thought: Need to seperate update_board() into player_turn() and update_board()
- 15m: Make PR, fix merge conflict in devlog.md

2023-09-03
- 1.5hr: Talk to Patrick about moving to functional programming and creating patrick-refactor branch

2023-09-04
- 5m: Review changes made in patrick-refactor branch 
- 5m: Make issues based on changes to given TODOs from patrick-refactor branch
- 5m: Start writing PR for patrick-refactor branch
- 25m: Complete writing PR for patrick-refactor branch
- 15m: Add additional comments in TODOs

2023-09-08
- 5m: On isWin/patrick-refactor branch, separate X and O win logic for horizontal win
- 5m: Make X and O seperate if and elif statements
- 10m: Update rest of elif statements
- 5m: Add isWin() with sample board to run
- 5m: Add test_suite()
- 5m: Add more specific print strings to test_suit() by win condition
- 5m: Fix bug in checkWin() for 'O's in horizontal win, bottom row
- 1hr: Implement the 'Wesley Blitz'

2023-09-22
- 5m: Review set-up after break
- 5m: Add wesley-blitz to seperate branch
- 5m: Remember how Python repl and interactive sessions work
- 10m: Test out get_player_move, update print() to show player's move and return statement
- 15m: Learn about combining split() and list comprehension to for player_move in get_player_move()
- 5m: Add split() and list comprehension to for player_move in get_player_move()
- 5m: Test running game, fix error in get_player_move by removing 'value' parameter
- 15: Write PR for merging get_player_move() branch into patrick_refactor branch
- 5m: Add print_board() to start_game(), decide on next feature to implement
- 10m: Review quote_repository data type and set-up
- 10m: Propose and discuss new implementatinon of quote_repository using as quote_repository(game_state) and a dictionary where game_state: ["quote 1", 'quote 2", "quote 3"]
- 5m: Start implemtning quote_repository as dictionary
- 5m: Test random.choice() and import random library
