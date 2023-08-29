#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add, count = 0, len(argv) - 1
    for i in range(1, (count + 1)):
        add = add + int(argv[i])
    print(add)
