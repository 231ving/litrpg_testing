"""
Testing how basic conlangs made using simple rules and ciphers look
"""


def reverse(text: str | list):
    print(text)
    if type(text) is str:
        tkns = text.split()
        temp = []
        for i in range(len(tkns)):
            temp.append(tkns[-i-1])
        print(" ".join(temp))

c = "He is coming"
reverse(c)