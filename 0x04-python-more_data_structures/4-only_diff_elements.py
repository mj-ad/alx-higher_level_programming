#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s = set()
    for i in set_1:
        if i not in s:
            s.add(i)

    for n in set_2:
        if n not in s:
            s.add(n)

    for i in set_1:
        for n in set_2:
            if i == n:
                s.remove(i)
    return s
