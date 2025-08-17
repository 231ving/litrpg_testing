"""
Testing how basic conlangs made using simple rules and ciphers look
"""


def reverse_order(text: str):
    """Reverses the order of a string"""
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


def reverse_str(text: str):
    """Reverses the individual characters of a string"""
    if type(text) is str:
        print(text)
        tkns = text.split()
        temp = []
        for word in tkns:
            temp_wrd = ""
            for i in range(len(word)):
                temp_wrd += word[-i - 1]
            temp.append(temp_wrd)
        text = " ".join(temp)
        print(text)
        print()
        return text
    else:
        print("Error, not a string\n")
        return


def vowel_shift(text: str, shift: int):
    """Shift cipher for vowels only"""
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


def consonant_shift(text: str, shift: int):
    """Shift cipher for consonants only"""
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


def insert_char_str(text: str, char: str, min_length: int, freq: int):
    """Insert a specified character into words of minimum length, up to the frequency amount"""
    if type(text) is str:
        if type(char) is str:
            print(text)
            tkns = text.split()
            temp = []
            for i in tkns:
                if len(i) >= min_length:
                    times = len(i) // min_length
                    temp_wrd = i
                    temp_tkns = []
                    for j in range(0, times + 1):
                        temp_tkns.append(temp_wrd[:min_length])
                        temp_wrd = temp_wrd[min_length:]
                    count = 0
                    for k in range(0, len(temp_tkns)):
                        if count < freq:
                            if len(temp_tkns[k]) == min_length:
                                temp_tkns[k] = temp_tkns[k] + char
                            count += 1
                    temp.append("".join(temp_tkns))
                else:
                    temp.append(i)
            text = " ".join(temp)
            print(text)
            return text
        else:
            print("Character to insert was not a string\n")
            return
    else:
        print("Text given was not a string\n")
        return


c = "He is coming, to say hello. Outrageous!"
#reverse_order(c)
#text1 = vowel_shift(c, 2)
#consonant_shift(text1, 1)
#reverse_str(c)
insert_char_str(c, "'", 3, 2)
