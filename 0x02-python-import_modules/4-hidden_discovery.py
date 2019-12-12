#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    list = dir(hidden_4)
    for wrd in list:
        if (wrd[:2] != '__'):
            print('{:s}'.format(wrd))
