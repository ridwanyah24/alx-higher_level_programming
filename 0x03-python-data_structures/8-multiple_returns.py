#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[:1] = None
        return (0, None)
    new_tup = []
    new_tup.append(len(sentence))
    new_tup.append(sentence[0])

    return tuple(new_tup)
