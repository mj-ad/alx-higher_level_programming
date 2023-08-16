#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = set()
    for i in set_1:
        for n in set_2:
            if i == n:
                s.add(i)
    return s
