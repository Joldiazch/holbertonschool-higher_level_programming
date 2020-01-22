#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            c = 0
            for i in range(len(line)):
                if line[i] == search_string[c]:
                    c += 1
                    if c == len(search_string):
                        line = line + new_string
                        break
                    continue
            f.write(line)
