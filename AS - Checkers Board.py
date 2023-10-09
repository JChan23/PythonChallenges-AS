rows = int(input('Please input the number of rows on the checkerboard: '))
columns = int(input('Please input the number of columns on the checkerboard: '))
checkerboard = [['.'] * columns for i in range(rows)]

for j in range(0, rows):
  for i in range(0, columns):
    if j % 2 == 0 and i % 2 == 1:
      checkerboard[j][i] = '*'
    if j % 2 == 1 and i % 2 == 0:
      checkerboard[j][i] = '*'

print('')
for j in range(0, rows):
    print(checkerboard[j], sep = ' ')

print('')
for j in range(0, rows):
  for i in range(0, columns):
      print(checkerboard[j][i], end = " ")
  print()
