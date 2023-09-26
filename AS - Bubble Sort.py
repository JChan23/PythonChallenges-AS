import random

array = [] 
for i in range(9):
  randomnum = random.randint(0, 100)
  array.append(randomnum)

length = len(array)
for i in range(length):
  for j in range(0, length - i - 1):
    if array[j] > array[j+1]:
      temp = array[j]
      array[j] = array[j+1]
      array[j+1] = temp
print(array)
