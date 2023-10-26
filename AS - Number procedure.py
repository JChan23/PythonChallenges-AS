#Create a procedure that outputs the sum and product of all the numbers in a list	
def arithmetic(array):
  total = 0
  product = 1
  for i in range(len(array)):
    total = total + array[i]
    product = product * array[i]
  print('Sum:', total)
  print('Product:', product)

arithmetic([45, 33, 25, 69, 56, 51, 7, 16, 44, 26, 92, 67, 61, 37, 39, 43, 72, 56, 68, 38])
