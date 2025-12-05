#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    if len(list) > 1:
        print("{:d} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{:d}: {}".format(i,argv[i]))
    elif len(argv) == 1:
        print("1 argument:".format(len(argv)))
        print("{}".format(dir(argv)))
    elif len(argv) == 0:
        print("0 argumnts.")

