#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        indicator = 0
        for char in text:
            if indicator is 1 and char is " ":
                continue

            if char in '.?:':
                print(char, end="")
                print("\n")
                indicator = 1
            else:
                print(char, end="")
                indicator = 0
        if indicator is 0:
            print()
