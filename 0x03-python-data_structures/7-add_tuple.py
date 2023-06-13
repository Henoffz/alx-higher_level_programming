#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tal = len(tuple_a)
    tbl = len(tuple_b)
    new_t = ()

    for i in range(2):
        if i >= tal:
            val_a = 0
        else:
            val_a = tuple_a[i]

        if i >= tbl:
            val_b = 0
        else:
            val_b = tuple_b[i]

        if i == 0:
            new_t = (val_a + val_b)
        else:
            new_t = (new_t, val_a + val_b)

    return new_t
