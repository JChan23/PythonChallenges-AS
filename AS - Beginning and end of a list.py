#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

array = [69, 5, 10, 15, 20, 25, 55, 654, 4965, 15, 11, 5]
new = []
new.append(array[0])
new.append(array[len(array)-1])
print(new)
