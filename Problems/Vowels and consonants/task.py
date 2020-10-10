vowel = ['a', 'e', 'i', 'o', 'u']
input_line = str(input())

for char in input_line:
    if not char.isalpha():
        break
    if char in vowel:
        print("vowel")
    else:
        print("consonant")
