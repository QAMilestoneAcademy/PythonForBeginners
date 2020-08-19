#Draw A Game Board Solutions

# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#
#### Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

board_size = int(input("What size of game board? "))

# Then, we need to draw each row of the game board. Each row consists of horizontal pieces (---) and vertical pieces (|). Each of these shows up in a pattern, so we can rely on for loops to help with the rendering.
#
# To print a single row, we want to do something like this:
#
# print(" --- " * board_size)

# To print the vertical parts of the row, we want something like this, because we don’t care about trailing whitespace, and because we want one more vertical line than the size of the board:

# print("|   " * (board_size + 1))

#Let's make use of for loop to get board as per board size:

for index in range(board_size):
    print(" --- " * board_size)
    print("|   " * (board_size + 1))
 #Since we want to close it with horizantal lines

print(" --- " * board_size)
