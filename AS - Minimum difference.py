#Output the minimum differences between any two numbers in an array

array = [85, 63, 26, 43, 36, 60, 47, 22, 19, 38, 65, 76, 27, 42, 80, 48, 95, 34, 87, 61]
array.sort()
min = 100000
print(array)

for i in range(0, len(array)-1):
  dif = array[i+1]-array[i]
  if dif < min:
    min = dif
print('')
print(min) #48-47 = 1
