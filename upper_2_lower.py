word="UBUnTU"

print(word.swapcase())
converted=""
# ASCII OF A=65
# ASCII OF Z=90
for letter in word:
    if 'A' <= letter <= 'Z':
        converted+=chr(ord(letter)+32)
    else:
        converted+=letter

print(converted)

#  ACSII values of A-Z = 65 to 90
#  ACSII values of a-z =97-122

#if letter is "A"
# then condition checks for 65<=65<=90 -> true 
# if letter is a then 65<=97<=90 -> false which is because of lower case letter.