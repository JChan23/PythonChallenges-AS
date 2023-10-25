import random

password = ''
letters = []
special = []
s = ['@', '!', '%', '$', '*', '&', '#']
for i in range(4):
  r = random.randint(0, 6)
  special.append(s[r])

colour = input('What is your favorite colour? ')
place = input('What is your favorite place? ')
animal = input('What is your favorite animal ')

for i in range (0, len(colour)):
  letters.append(colour[i:i+1])
for i in range (0, len(place)):
  letters.append(place[i:i+1])
for i in range (0, len(animal)):
  letters.append(animal[i:i+1])
random.shuffle(letters)

for i in range(0, len(letters)):
  password = password + letters[i]
for i in range(4):
  password = password + special[i]
print('')
print(password)
