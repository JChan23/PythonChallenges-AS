denary = input('Input a denary number: ') 
BCD = ''

for i in range(0, len(denary)):
  if denary[i] == '0':
    BCD = BCD+'0000 '
  elif denary[i] == '1':
    BCD = BCD+'0001 '
  elif denary[i] == '2':
    BCD = BCD+'0010 '
  elif denary[i] == '3':
    BCD = BCD+'0011 '
  elif denary[i] == '4':
    BCD = BCD+'0100 '
  elif denary[i] == '5':
    BCD = BCD+'0101 '
  elif denary[i] == '6':
    BCD = BCD+'0110 '
  elif denary[i] == '7':
    BCD = BCD+'0111 '
  elif denary[i] == '8':
    BCD = BCD+'1000 '
  elif denary[i] == '9':
    BCD = BCD+'1001 '

print(BCD)
