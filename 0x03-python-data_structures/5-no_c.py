#!/usr/bin/env python3
def no_c(my_string):
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            ret += my_string[i]
        return ret
