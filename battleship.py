#!/usr/bin/python
from random import randint
from collections import defaultdict

class BattleBoard(object):
    def __init__(self, name, board_size, num_ships):
        self.player_ships = defaultdict(list)
        self.board = []
        self.coords = []
        self.name = name
        self.board_size = int(board_size)
        self.num_ships = int(num_ships)
    def create_board(self):
        for x in range(self.board_size):
            self.board.append(["O"] * self.board_size)
    def print_board(self):
        print self.name + "'s Board"
        for row in self.board:
          print " ".join(row)
    def random_ships(self):
        for ships in range(self.num_ships):
            x_coord = randint(0, len(self.board) - 1)
            y_coord = randint(0, len(self.board) - 1)
            self.player_ships[ships].append([x_coord, y_coord])

# Initialize the game
board_size = 5
num_turns = 5
num_ships = raw_input("Number of ships in the game?")
firstplayer_name = raw_input("First Players name? ")
secondplayer_name = raw_input("Second Players name? ")
firstplayer = BattleBoard(firstplayer_name, board_size, num_ships)
firstplayer.create_board()
firstplayer.random_ships()
secondplayer = BattleBoard(secondplayer_name, board_size, num_ships)
secondplayer.create_board()
secondplayer.random_ships()

print "First Player Ship location"
print firstplayer.player_ships

print "Second Player Ship location"
print secondplayer.player_ships

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
    