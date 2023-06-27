#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_IntPrinted = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_IntPrinted += 1
        except (ValueError, TypeError):
            i += 1
            continue
    print("")
    return num_IntPrinted
