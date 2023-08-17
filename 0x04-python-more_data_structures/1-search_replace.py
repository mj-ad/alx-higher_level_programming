#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new = my_list.copy()
        for n in new:
            if n == search:
                i = new.index(n)
                new[i] = replace
        return new
    else:
        return list()
