import math
def LEFT(string,length):   
    return string[0:length]

def RIGHT(string,length):
    return string[-length::]

def MID (string,start,end):
    return string[start-1:start+end-1]
    
def LENGTH (string):
    return len(string)

def LCASE (character):  
    return character.lower()
    
def UCASE(character):
    return character.upper()

def TO_UPPER(string):
    return string.upper()
 
def TO_LOWER(string):
    return string.lower()
 
def NUM_TO_STRING(num):
    return str(num)

def STRING_TO_NUM(string):
    return float(string)

def INT(num):
    return math.floor(num)

def ASC(char):
    return ord(char)
  
 
my_string = LEFT("abcdefg",3)
print(my_string)

my_string = RIGHT("abcdefg",3)
print(my_string)

my_string = MID("abcdefg", 3, 4)
print(my_string)

my_string = LENGTH("abcdefg")
print(my_string)

my_character = LCASE("A")
print(my_character)

my_character = UCASE("a")
print(my_character)

my_string = TO_UPPER("ABCDefg 123")
print(my_string)

my_string = TO_LOWER("ABCDefg 123")
print(my_string)

my_string = NUM_TO_STRING(10)
print(my_string)
print('I ate '+my_string+' berries')

my_num = STRING_TO_NUM("20.5")
print(my_num)
print(my_num+21.5)

my_num = INT(24.5645)
print(my_num)

my_character = ASC("A")
print(my_character)
