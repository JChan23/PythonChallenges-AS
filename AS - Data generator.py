import datetime

def integer():
  return 69

def string():
  return 'Hello World!'

def boolean():
  return 'TRUE'

def real():
  return 3.14159

def char():
  return 'A'

def date():
  return datetime.datetime(2023, 7, 12)

data = input('What data type would you like to see an example of? ')

if data == 'integer':
  print(integer())
elif data == 'string':
  print(string())
elif data == 'boolean':
  print(boolean())
elif data == 'real':
  print(real())
elif data == 'char':
  print(char())
elif data == 'date':
  print(date())
else:
  print('Error. Invalid data type. Please try again.')
