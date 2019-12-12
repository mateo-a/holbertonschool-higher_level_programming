#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
        len_arg = len(argv)
        if len_arg == 1:
                print("0 arguments.")
        elif len_arg == 2:
                print("1 argument:")
                print("1: {}".format(argv[1]))
        elif len_arg > 2:
                print("{} arguments:".format(len_arg - 1))
                for i in range(1, len_arg):
                        print("{}: {}".format(i, argv[i]))
