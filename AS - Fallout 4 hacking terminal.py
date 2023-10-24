#In the game Fallout 4 you are expected to crack codes. It is similar to hangman. The game includes a word list and tells you a likeness compared to the actual word. For it to be like the actual word not only must the letter be in the word, but also in the same position. To do this in Python you will need to type in the word and check it.	
import random

words = [
    'BAKER', 'CIDER', 'DINER', 'FABLE', 'HAZEL',
    'GIVER', 'JOLLY', 'LIVER', 'MUTED', 'NOBLE',
    'OCEAN', 'PIXEL', 'QUILT', 'RIDER', 'SABER',
    'TABLE', 'VOCAL', 'WIDER', 'YACHT', 'ZESTY',
    'AMBER', 'BLITZ', 'CRISP', 'DAISY', 'EAGLE',
    'FLOOD', 'GRAPE', 'HASTE', 'INPUT', 'JOKER',
    'KNEAD', 'LEMON', 'MANGO', 'NUDGE', 'ONION',
    'PENNY', 'QUERY', 'ROVER', 'SWEAT', 'TRICK',
    'USURY', 'VIVID', 'WOVEN', 'XEROX', 'YIELD',
    'ZEBRA', 'ALIEN', 'BRACE', 'CRANE', 'DWELL'
]


lives = 4
random15 = []

while len(random15) < 15:
  r = words[random.randint(0, 49)]
  if r not in random15:
    random15.append(r)

RandomWordIndex = random.randint(0, 14)
word = random15[RandomWordIndex]


print('To play: A list of words will be given to you below. One of teh words has been picked as the correct answer. Try and guess the word. You have 4 lives. If you get it wrong, we will tell you how many letters of the word is actually similar to the right answer. Goodluck.')
print('Example: Guess=MAYBE, Answer=MALES, likeness=2')
while lives != 0:
  hint = 0
  print('')
  print('List of words:', random15)
  print('Lives left:', lives)
  print('')
  guess = input('Please input your guess: ')
  guess = guess.upper()
  #compare guess and word
  if guess == word:
    print('')
    print('Correct. You Win!')
    break
  else:
    GuessWordLetters = []
    RandomWordLetters = []
    for i in range(5):
      RandomWordLetters.append(word[i:i+1])
      GuessWordLetters.append(guess[i:i+1])
    for u in range(5):
      if RandomWordLetters[u] == GuessWordLetters[u]:
        hint = hint + 1
    print('Incorrect. Likeness:', hint)
    lives = lives - 1
    random15.remove(guess)

if lives == 0:
  print('')
  print('You lost. The correct answer was:', word)
