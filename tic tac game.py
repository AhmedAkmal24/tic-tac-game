import random

board = ['-', '-', '-', 
         '-', '-', '-', 
         '-', '-', '-']

CurrentPly = 'X'
Winner = None
gamerunning = True

def printboard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('--------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('--------')
    print(board[6] + '|' + board[7] + '|' + board[8])

printboard(board)


def InputPly(board):
    inp=int(input('enter a number between 1-9 : '))
    if inp >=1 and inp <=9 and board[inp-1] == '-':
        board[inp-1]=CurrentPly
    else:
        print('oops this place is taken.')

def checkhor(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "-":
           winner = board[0]
           return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
           winner = board[3]
           return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
           winner = board[6]
           return True

def checkrow(board):
     global Winner 
     if board[0] == board[3] == board[6] and board[0] != '-':
          Winner = board[0]
          return True
     elif board[1] == board[4] == board[7] and board[1] != '-':
          Winner = board[1]
          return True
     elif board[2] == board[5] == board[8] and board[2] != '-':
          Winner = board[2]
          return True
     
def chechdia(board):
     global Winner
     if board[0] == board[4] == board[8] and board[0] != '-':
          Winner = board[0]
          return True
     elif board[2] == board[4] == board[6] and board[2] != '-':
          Winner = board[2]
          return True

def checktie(board):
     global gamerunning
     if '-' not in board :
          print(board)
          print('it is a tie')
          gamerunning = False
def checkwin():
     global gamerunning
     if chechdia(board) or checkhor(board) or checkrow(board):
          print(f'the winner is {Winner}.')
          gamerunning = False


def switchply():
     global CurrentPly
     if CurrentPly == 'X':
          CurrentPly = 'O'
     else:
          CurrentPly = 'X'          
def computer(board):
     while CurrentPly == 'O':
          pos = random.randint[0 ,8]
          if board[pos]=='-':
              board[pos] = 'O'
              switchply()

while gamerunning :
    printboard(board)
    InputPly(board)
    checkwin()
    checktie(board)
    switchply()
    computer(board)
    checkwin()
    checktie(board)