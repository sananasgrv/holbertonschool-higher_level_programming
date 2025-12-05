#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    SUM = 0
    for i in range(len(argv)):
        SUM += int(i)
        print(SUM)
