#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_arg = len(argv)
    total = 0
    for i in range(1, len_arg):
        total += int(argv[i])
    print("{}".format(total))
