#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    c = len(argv)
    print("{:d} {:s}{:s}".format(c - 1, "argument" if c <= 2 else "arguments",
                                 "." if c == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
