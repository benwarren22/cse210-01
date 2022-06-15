def main():
   board = ["1","2","3","4","5","6","7","8","9"]
   player = "X"
   i = 1
   while  (winner(board) and draw(board, i)):
      boarddisplay(board)
      playerinput(player, board)
      player = playerturn(player)
   boarddisplay(board)
   player = playerturn(player)
   if (winner(board) == False):
      print("Player "+player+" wins! Thanks for playing!")
   else: print("Draw!")

def playerturn(player):
   if player == "X":
      return "O"
   elif player == "O":
      return "X"

def playerinput(player, board):
   
   i = int(input("Player "+player+", choose a square between 1-9: "))
   board[i - 1] = player

def boarddisplay(board):
  
   print()
   print("  "+board[0]+"  |  "+board[1]+"  |  "+board[2])
   print("-----+-----+-----")
   print("  "+board[3]+"  |  "+board[4]+"  |  "+board[5])
   print("-----+-----+-----")
   print("  "+board[6]+"  |  "+board[7]+"  |  "+board[8])
   print()

def draw(board, i):
   for i in range(9):
      if board[i] != "X" and board[i] != "O":
         return True
   return False

def winner(board):
   if (board[0] == board[1] == board[2] or
      board[3] == board[4] == board[5] or 
      board[6] == board[7] == board[8] or 
      board[0] == board[3] == board[6] or
      board[1] == board[4] == board[7] or
      board[2] == board[5] == board[8] or
      board[2] == board[4] == board[6] or
      board[0] == board[4] == board[8]):
      return False
   return True

if __name__ == "__main__":
    main()