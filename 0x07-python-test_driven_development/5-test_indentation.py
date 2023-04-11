#!/usr/bin/python3


def text_indentation(text):
    """ the function prints a text with two new lines after each of these
    characters . ? and :
    text must be a string otherwise raise a TypeError: text must be a string
    there should be no space at the beginning or at the end of each printed line
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    test = ".?:"

    for i in range(len(text)):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in test:
            if text[i] in test:
                print("\n")
            continue
