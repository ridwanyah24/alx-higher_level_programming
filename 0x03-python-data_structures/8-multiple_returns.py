#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    new_tup = []
    new_tup.append(len(sentence))
    new_tup.append(sentence[0])

    return tuple(new_tup)
