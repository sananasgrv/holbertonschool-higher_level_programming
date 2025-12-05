#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    SUM = 0
    for i in range(1, len(argv)):
        SUM += int(argv[i])
    print(SUM)
