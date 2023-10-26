#Create a Caesar Cipher encoder and decoder.
def LinearSearch():
  for i in range(0, len(alphabet)):
    if (alphabet[i] == char):
      return int(i)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = ''
position = 0

print('Program only takes lowercase text\n')
type = input('Would you like to encrypt or decrypt you text? ')
text = input('Please enter your text: ')

if type == 'encrypt':
  shift = int(input('How many places do you want the text to be shifted? '))
  for i in range(len(text)):
    char = text[i]
    if char == ' ':
      result = result + ' '
    else:
      position = (LinearSearch() + shift)  % 26
      result = result + alphabet[position]
elif type == 'decrypt':
  shift = int(input('How many places was your text shifted? '))
  for i in range(len(text)):
    char = text[i]
    if char == ' ':
      result = result + ' '
    else:
      position = (LinearSearch() - shift) % 26
      result = result + alphabet[position]

print(result)
