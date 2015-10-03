#!/usr/bin/python
from random import randint

class battleboard(object):

    def __init__(self, name, board_size, board, num_ships):
        self.name = name
        self.board_size = board_size
        self.board = board
        self.num_ships = num_ships

    def create_board(self):
        for x in range(self.board_size):
            self.board.append(["O"] * board_size)

    def print_board(self):
        print self.name + "'s Board"
        for row in self.board:
            print " ".join(row)

    def random_row(self):
        for ships in range(self.num_ships):
            shipsrandint(0, len(self.board) - 1)

    def random_col(self):
        return randint(0, len(self.board) - 1)

# Initialize the game
board_size = 5
num_turns = 5
board = []
firstplayer_name = raw_input("First Players name? ")
secondplayer_name = raw_input("Second Players name? ")
firstplayer = battleboard(firstplayer_name, board_size, board)
secondplayer = battleboard(secondplayer_name, board_size, board)
firstplayer.create_board()
secondplayer.create_board()
first_ship_row = firstplayer.random_row()
first_ship_col = firstplayer.random_col()
second_ship_row = secondplayer.random_row()
second_ship_col = secondplayer.random_col()

print "First Player Ship location"
print first_ship_row
print first_ship_col

print "Second Player Ship location"
print second_ship_row
print second_ship_col

print "Let's play Battleship!"

firstplayer.print_board()
secondplayer.print_board()

# Lets run the game
for turn in range(num_turns):
    # Print (turn + 1) here!
    print "Turn", turn + 1
    # Make a guess
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    #Evaluate guess
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row-1][guess_col-1] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row-1][guess_col-1] = "X"
    print_board(board)
    if turn == 3:
        print "Game Over"    
    