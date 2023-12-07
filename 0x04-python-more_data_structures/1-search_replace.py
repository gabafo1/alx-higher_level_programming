#!/usr/bin/python
def search_replace(my_list, search, replace):
    return list(map(lamda e: replace if e == search else e, my_list))
