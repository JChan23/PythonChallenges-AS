array = [[2, 5, 6], [1, 2, 3], [8, 22, 5]]
max = 0
column = 0
row = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] > max:
            max = array[i][j]
            row = i
            column = j

print(max)
print(row, col
