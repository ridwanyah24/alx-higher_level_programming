#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    def arguments():
        if len(argv) == 1:
            print("{} arguments.".format(len(argv) - 1))
        else:
            print("{} argument:".format(len(argv) - 1))
        for i in range(1, (len(argv))):
            print("{}: {}".format(i ,argv[i]))

    arguments()
