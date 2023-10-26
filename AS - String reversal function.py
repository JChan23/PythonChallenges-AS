#Create a function that returns the reverse of a string	
def reverse(str):
  return str[::-1]

word = input('Enter word to reverse: ')
print(reverse(word))
