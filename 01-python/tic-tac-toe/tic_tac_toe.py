import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals) 
    
    
    if self.board[0]== self.board[1] and self.board[2]== self.board[1]and self.board[0]!= None:
        self.is_game_over=True
    elif self.board[0]== self.board[3] and self.board[3]== self.board[6]and self.board[0]!= None:
        self.is_game_over=True
    elif self.board[1]== self.board[4] and self.board[4]== self.board[7]and self.board[1]!= None:
        self.is_game_over=True
    elif self.board[2]== self.board[5] and self.board[5]== self.board[8]and self.board[2]!= None:
        self.is_game_over=True
    elif self.board[3]== self.board[4] and self.board[4]== self.board[5]and self.board[3]!= None:
        self.is_game_over=True
    elif self.board[6]== self.board[7] and self.board[7]== self.board[8]and self.board[6]!= None:
        self.is_game_over=True
    elif self.board[0]== self.board[4] and self.board[4]== self.board[8]and self.board[0]!= None:
        self.is_game_over=True
    elif self.board[6]== self.board[4] and self.board[4]== self.board[2]and self.board[6]!= None:
        self.is_game_over=True
        
    return self.is_game_over

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL
    self.is_over()
    if self.is_game_over==True:
        self.winner="h"
    

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied
    
    i= 4
    
    if self.board[i] is not None: 
        while True:
            i= random.randint(0, 8)
            if self.board[i] is None:
                break
    self.board[i]= _MACHINE_SYMBOL
    
    self.is_over()
    if self.is_game_over==True:
        self.winner="m"
    
# =============================================================================
#     for i, cell in enumerate(self.board):
#       if cell is None:
#         self.board[i] = _MACHINE_SYMBOL
#         break
# =============================================================================

  def format_board(self):
    # TODO: Implement this function, it must be able to print the board in the following format:
    #  x|o| 
    #   | | 
    #   | | 
    print(self.board[0],self.board[1],self.board[2],sep='|')
    print(self.board[3],self.board[4],self.board[5],sep='|')
    print(self.board[6],self.board[7],self.board[8],sep='|')
   

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    self.format_board()
    print()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if self.winner=="m":
        print("pierdes")
    elif self.winner == "h":
        print("ganas")

    pass
