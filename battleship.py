#!/usr/bin/python
from random import randint
from collections import defaultdict

class BattleBoard(object):
    def __init__(self, name, board_size, num_ships):
        self.player_ships = defaultdict(list)
        self.board = []
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
        flag = False
        ship = 0
        temp_coords = []
        while ship < self.num_ships:
            temp_coords = randint(1, len(self.board)), randint(1, len(self.board))
            # Make sure coordinates are unique
            for scan_ship in range(self.num_ships):
                if self.player_ships[scan_ship] == [temp_coords]:
                    flag = True  
            if flag == False:
                self.player_ships[ship].append(temp_coords)
                ship = ship + 1
            flag = False


# Initialize the game
num_ships = int(raw_input("Number of ships in the game?"))
board_size = 5 + num_ships - 1
num_turns = num_ships * 3
player_turn = 0
firstplayer_name = raw_input("First Players name? ")
secondplayer_name = raw_input("Second Players name? ")
firstplayer = BattleBoard(firstplayer_name, board_size, num_ships)
firstplayer.create_board()
firstplayer.random_ships()
secondplayer = BattleBoard(secondplayer_name, board_size, num_ships)
secondplayer.create_board()
secondplayer.random_ships()
# Cheat
print "First Player Ship location"
print firstplayer.player_ships
print "Second Player Ship location"
print secondplayer.player_ships

print "Let's play Battleship!"
firstplayer.print_board()
secondplayer.print_board()
# Lets run the game
for turn in range(num_turns * 2):
    # switch turns
    if player_turn == 0:
        print ("Player %s Turn %s" % (firstplayer_name, turn + 1))
        currentplayer = secondplayer
        player_turn = 1
    else:
        print ("Player %s Turn %s" % (secondplayer_name, turn + 1))
        currentplayer = firstplayer
        player_turn = 0
    turn_ship = 0
    turn_hit = False
    # Make a guess
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    #Evaluate guess
    if (guess_row < 1 or guess_row > board_size) or (guess_col < 1 or guess_col > board_size):
        print "Oops, that's not even in the ocean."
    elif(currentplayer.board[guess_row-1][guess_col-1] == "X"):
        print "You guessed that one already."
    elif(currentplayer.board[guess_row-1][guess_col-1] == "S"):
        print "You sank that ship already."
    else:
        turn_coords = [(guess_row, guess_col)]
        for scan_hit in range(num_ships):
            if cmp(currentplayer.player_ships[scan_hit], turn_coords) == 0:
                currentplayer.board[guess_row-1][guess_col-1] = "S"
                currentplayer.num_ships=currentplayer.num_ships-1
                print "Congratulations! You sunk a battleship!" 
                turn_hit = True
        if turn_hit == False:
            print "You missed my battleship!"
            currentplayer.board[guess_row-1][guess_col-1] = "X"
    currentplayer.print_board()
    print "%s has %s out of %s battleships left" % (currentplayer.name, currentplayer.num_ships, num_ships)
    if currentplayer.num_ships == 0:
        print "%s has lost!" % (currentplayer.name)
        break
print "Game Over"
    