board = [['', '', ''], ['', '', ''], ['', '', '']]
count = 0
row = 0
column = 0
win = ''

while count != 9:
  print('\nCurrent board:')
  for i in range(3):
    print(board[i])
    
  if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
    print('P1 wins')
    break
  elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
    print('P1 wins')
    break
  elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
    print('P1 wins')
    break
  elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
    print('P1 wins')
    break
  elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
    print('P1 wins')
    break
  elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
    print('P1 wins')
    break
  elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
    print('P1 wins')
    break
  elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
    print('P1 wins')
    break
  elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
    print('P2 wins')
    break
  elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
    print('P2 wins')
    break
  elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
    print('P2 wins')
    break
  elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
    print('P2 wins')
    break
  elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
    print('P2 wins')
    break
  elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
    print('P2 wins')
    break
  elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
    print('P2 wins')
    break
  elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
    print('P2 wins')
    break
  
  if count % 2 == 0:
    row = int(input("\nPlayer1's move. Which row would you like your 'X' to be in? Input a value from 1-3: "))
    row = row - 1
    column = int(input("Which column would you like your 'X' to be in? Input a value from 1-3: "))
    column = column - 1
    board[row][column] = 'X'
  else:
    row = int(input("\nPlayer2's move. Which row would you like your 'O' to be in? Input a value from 1-3: "))
    row = row - 1
    column = int(input("Which column would you like your 'O' to be in? Input a value from 1-3: "))
    column = column - 1
    board[row][column] = 'O'
  count = count + 1

print('\nCurrent board:')
for i in range(3):
  print(board[i])
if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
  print('P1 wins')
elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
  print('P1 wins')
elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
  print('P1 wins')
elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
  print('P1 wins')
elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
  print('P1 wins')
elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
  print('P1 wins')
elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
  print('P1 wins')
elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
  print('P1 wins')
elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
  print('P2 wins')
elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
  print('P2 wins')
elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
  print('P2 wins')
elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
  print('P2 wins')
elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
  print('P2 wins')
elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
  print('P2 wins')
elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
  print('P2 wins')
elif board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
  print('P2 wins')
else:
  win = 'false'



if count == 9 and win == 'false':
  print('Draw game')
