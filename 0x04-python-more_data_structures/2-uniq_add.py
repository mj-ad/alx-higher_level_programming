#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        new = []

        for i in my_list:
            if i in new:
                continue
            else:
                new.append(i)
                sum += i
    return sum
