"""
Testing how basic conlangs made using simple rules and ciphers look
"""


def reverse(text: str):
    if type(text) is str:
        print(text)
        tkns = text.split()
        temp = []
        for i in range(len(tkns)):
            temp.append(tkns[-i-1])
        print(" ".join(temp))
        print()
        return " ".join(temp)
    else:
        print("Error, not a string\n")
        return


def vowel_replace(text: str, shift: int):
    vowels = 'aeiou'
    lower_vowels = [i for i in vowels]
    upper_vowels = [i.upper() for i in vowels]
    if type(shift) is not int:
        print("Shift must be a integer\n")
        return
    if type(text) is str:
        print(text)
        text = [i for i in text]
        for i in range(len(text)):
            if text[i] in lower_vowels:
                text[i] = lower_vowels[(lower_vowels.index(text[i]) + shift) % 5]
            if text[i] in upper_vowels:
                text[i] = upper_vowels[(upper_vowels.index(text[i]) + shift) % 5]
        text = "".join(text)
        print(text)
        print()
        return text
    print("Text given was not a string\n")
    return


def consonant_replace(text: str, shift: int):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    lower_consonants = [i for i in consonants]
    upper_consonants = [i.upper() for i in consonants]
    if type(shift) is not int:
        print("Shift must be a integer\n")
        return
    if type(text) is str:
        print(text)
        text = [i for i in text]
        for i in range(len(text)):
            if text[i] in lower_consonants:
                text[i] = lower_consonants[(lower_consonants.index(text[i]) + shift) % 21]
            if text[i] in upper_consonants:
                text[i] = upper_consonants[(upper_consonants.index(text[i]) + shift) % 21]
        text = "".join(text)
        print(text)
        print()
        return text
    print("Text given was not a string\n")
    return


c = "He is coming, to say hello. Outrageous!"
reverse(c)
text1 = vowel_replace(c, 2)
consonant_replace(text1, 1)
