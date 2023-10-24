MyArray = ['A', 'B', 'C', 'D', 'E']

def LinearSearch():
  for position in range(0, len(MyArray)):
    if MyArray[position] == item:
      return position
  return -1

item = input('Enter an item to search for in the array: ')
if LinearSearch() == -1:
  print("Can't Find it!")
else:
  print("Found it at position", LinearSearch())
