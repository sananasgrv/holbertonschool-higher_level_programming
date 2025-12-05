#!/usr/bin/python3
def arg():
    list=dir()
    if len(list) > 1:
        print("{:d} arguments:".format(len(list)))
        for i in range(len(list)):
            print("{:d}: {}".format(i,list[i]))
    elif len(list) == 1:
        print("{:d} argument:".format(len(list)))
        print("{}".format(dir(list)))
    elif len(list) == 0:
        print("{:d} argumnts.")
    return 0
