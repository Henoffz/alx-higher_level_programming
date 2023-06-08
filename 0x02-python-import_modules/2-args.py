#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_list = "{} argument"
    argc = len(sys.argv) - 1
    if argc == 0:
        args_list += 's.'
    elif argc == 1:
        args_list += ':'
    else:
        args_list += 's:'
    print(args_list.format(argc))

    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
