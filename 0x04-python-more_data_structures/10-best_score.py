#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = []
        for k in a_dictionary:
            keys.append(k)
        base = a_dictionary[keys[0]]
        for i in range(len(keys)):
            if a_dictionary[keys[i]] > base:
                base = a_dictionary[keys[i]]
        for x in a_dictionary:
            if a_dictionary[x] == base:
                return x
    return None
