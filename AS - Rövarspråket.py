#This is a SUPER-SECRET language. Rövarspråket is not very complicated: you take an ordinary word and replace the consonants with the consonant doubled and with an "o" in between. So the consonant "b" is replaced by "bob", "r" is replaced with "ror", "s" is replaced with "sos", and so on. Vowels are left intact. It's made for Swedish, but it works just as well in English.	

text = input('Enter text for conversion: ')
text.lower()
final = ''
temp = ''
count = 0
for i in range(len(text)):
  if text[i] != 'a' and text[i] != 'e' and text[i] != 'i' and text[i] != 'o' and text[i] != 'u' and text[i] != ' ':
    temp = temp + text[i]
    count = count + 1
  else:
    if count == 0:
      final = final + text[i]
    else:
      final = final + temp + 'o' + temp + text[i]
      temp = ''
      count = 0

print(final)
