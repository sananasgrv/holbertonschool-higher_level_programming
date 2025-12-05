#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    if len(argv) > 1:
        print("{:d} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{:d}: {}".format(i+1, argv[i]))
    elif len(argv) == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("0 arguments.")
