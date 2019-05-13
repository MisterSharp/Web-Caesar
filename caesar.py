def alphabet_position(a):
    letters = {}
    for i in range(26):
        x = i + 97
        letters[chr(x)] = i
    if a.isupper(): 
        return letters.get(a.lower())
    else:
        return letters.get(a)

def rotate_character(char, rot):
    test_char = str(char) 
    if not test_char.isalpha():
        return char
    x = ((alphabet_position(char)) + rot) % 26
    if test_char.isupper():
        return chr(x + 65)
    return chr(x + 97)

def rotate_string(text, rot):
    string = ''
    for char in text:
        string += rotate_character(char, rot)
    return string
