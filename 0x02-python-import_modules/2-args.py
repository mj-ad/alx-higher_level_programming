#!usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    i = 1

    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        print("{} argument:".format(count-1))
    else:
        print("{} arguments:".format(count-1))

    while (i < count):
        print("{}: {}".format(i, argv[i]))
        i += 1
