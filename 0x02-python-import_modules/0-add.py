#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    sys.modules['0_add'] = None
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
