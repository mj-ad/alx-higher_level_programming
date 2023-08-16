#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        new = []
        sum = 0

        for i in my_list:
            if i in new:
                continue
            else:
                new.append(i)
                sum += i
    return sum
