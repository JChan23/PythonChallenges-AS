#Exercise 1
ringgit = 129
print(f"RM{ringgit}")
print('')

#Exercise 2
headings = ('column 1','column 2','column 3')
numcol1 = [1,25,241]
numcol2 = [442,526,11]
numcol3 = [234,2,4632]

print(f"{headings[0]:<15} {headings[1]:<15} {headings[2]:<15}")
for i in range(3):
    print(f"{numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")
print('')

#Exercise 3
number = int(input('Please enter a denary number to convert to binary: '))
print(f"Decimal: {number:d}\nBinary: {number:b}")
