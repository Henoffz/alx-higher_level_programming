#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_sum = 0

    for i in range(1, len(sys.argv)):
        arg_sum += int(sys.argv[i])
    print(arg_sum)
