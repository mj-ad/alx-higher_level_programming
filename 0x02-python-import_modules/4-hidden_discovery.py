#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as h
    for i in h:
        if i[0] == '_':
            continue
        else:
            print(i)
