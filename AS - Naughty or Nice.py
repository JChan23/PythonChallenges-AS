#Work out which children are Naughty or Nice in this string based challenge.	
#https://adventofcode.com/2015/day/5

def christmas(str):
  str.lower()
  letters = []
  count = 0
  test = ''
  for i in range(len(str)):
    letters.append(str[i])
  for i in range(len(letters)):
    if letters[i] == 'a' or letters[i] == 'e' or letters[i] == 'i' or letters[i] == 'o' or letters[i] == 'u':
      count = count + 1
  if count < 3:
    return 'String is naughty'
  count = 0
  for i in range(len(letters)-1):
    if letters[i] == letters[i+1]:
      count = count + 1
  if count < 1:
    return 'String is naughty'
  count = 0
  for i in range(len(letters)-1):
    test = letters[i] + letters[i+1]
    if test == 'ab' or test == 'cd' or test == 'pq' or test == 'xy':
      count = count + 1
  if count > 0:
    return 'String is naughty'
  else:
    return 'String is nice'

string = input('Enter a string for checking: ')
print(christmas(string))
