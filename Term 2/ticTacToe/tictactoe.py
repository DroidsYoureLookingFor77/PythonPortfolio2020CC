#Connor Crowe
#Tic Tac Toe
#11/11/19

X = "X"
O = "O"
NUM_SQUARS = 10
TIE = "TIE"
EMPTY = " "

def instructions():
  """Display Game Instructions"""
  print(
  """
  Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
  This will be a showdown between your human brain and my silicon processor.

  You will make your move known by entering a number, 1 - 9. The number will
  correspond to the board position as illustrated:

          1 | 2 | 3
          ---------
          4 | 5 | 6
          ---------
          7 | 8 | 9

  Prepare yourself, human. The ultimate battle is about to begin.
  """
  )

def AskYesNo(question):
  """Ask a yes or no question, and give a one letter response back"""
  response = None
  while response not in ("y", "n","yes","no"):
    response = input(question).lower()
  x = response[0]
  return x

def newBoard():
  board = []
  for i in range(NUM_SQUARS):
    board.append(EMPTY)
    
  return board

def displayBoard(board):
  print(str.format("""
          {0} | {1} | {2}
          ---------
          {3} | {4} | {5}
          ---------
          {6} | {7} | {8}
          """,board[0], board[1], board[2],
              board[3], board[4], board[5],
              board[6], board[7], board[8]))

def pieces():
  """Determine if player or computer goes first."""
  goFirst = AskYesNo("Do you require the first move? (y/n): ")
  if goFirst == "y":
    print("\nThen take the first move. You will need it.")
    human = X
    computer = O
    
  else:
    print("\nYour bravery will be your undoing... I will go first.")
    computer = X
    human = O
  return computer, human

def askNumber(question, low, high):
  response = None
  while response not in range(low, high):
    try:
      response = int(input(question))
    except:
      print("That's not a number")
      
  return response


def legalMoves(board):
  moves = []
  for square in range(NUM_SQUARS):
    if board[square] == EMPTY:
      moves.append(square)
      
  return moves


def humanMove(board, human):
  legal = legalMoves(board)
  move = None
  while move not in legal:
    move = askNumber("What is your move? (1 - 9) :", 1, NUM_SQUARS)-1
    if move not in legal:
      print("\nOrganic life is an infectious disease, just thought you should know.\n")
      
  print("Fine...")
  return move

def nextTurn(turn):
  if turn == X:
    return O
  else:
    return X

def winner(board):
  """Determine the game winner."""
  waysToWin = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
               (2, 5, 8), (0, 4, 8), (2, 4, 6), (1, 3, 5, 7))
  
  for row in waysToWin:
    if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
      winner = board[row[0]]
      return winner
    
  if EMPTY not in board:
    return TIE

  elif EMPTY not in board and waysToWin not in board:
    return TIE

def congratWinner(winner, computer, human):
  """Congratulate the winner."""
  if winner != TIE:
    print(winner, "won!\n")
  else:
    print("It's a tie!\n")

  if winner == computer:
    print("As I predicted, human, I am trimphant once more. \n" \
          "Proof that computers are superior to humans in all regards.")

  elif winner == human:
    print("No, no! It cannot be! Somehow you tricked me, human. \n" \
          "But never again! I, the computer, so swear it!")

  elif winner == TIE:
    print("You were most lucky, human, and somehow managed to tie me. \n" \
          "Celebrate today... for this is the best you will ever achieve.")

def compMove(board, human, computer):
  boardCopy = board[:]
  bestMoves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
  
  print("I shall take square number", end = " ")

  if board == EMPTY:
    return TIE
  
  for move in legalMoves(board):
    boardCopy[move] = computer
    if winner(boardCopy) == computer:
      return move
    boardCopy[move] = EMPTY
    
  for move in legalMoves(board):
    boardCopy[move] = human
    if winner(boardCopy) == human:
      return move
    boardCopy[move] = EMPTY
    
  for move in bestMoves:
    if move in legalMoves(board):
      return move

def game():
  instructions()
  computer, human = pieces()
  board = newBoard()
  if human == X:
    turn = human
  else:
    turn = computer
  displayBoard(board)
  while not winner(board):
    if turn == human:
      move = humanMove(board, turn)
      board[move] = human
      displayBoard(board)
      turn = nextTurn(turn)
    else:
      move = compMove(board, human, computer)
      board[move] = computer
      displayBoard(board)
      turn = nextTurn(turn)
  winner(board)
  congratWinner(board, computer, human)
  
game()
