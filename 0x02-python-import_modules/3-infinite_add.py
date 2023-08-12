#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    sum = 0

    for i in range(1, count):
        sum = int(argv[i]) + sum

    print({}.format(sum))