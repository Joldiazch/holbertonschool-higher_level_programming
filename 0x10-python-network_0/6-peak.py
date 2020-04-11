#!/usr/bin/python3


def sort_list(lis, start, end):
    """ sort a llist """
    if (end - start) < 1:
        return True

    pivot = lis[end]
    i = start
    for idx in range(start, end + 1):
        if lis[idx] < pivot:
            lis[i], lis[idx] = lis[idx], lis[i]
            i += 1

    if pivot < lis[i]:
        lis[i], lis[end] = lis[end], lis[i]

    sort_list(lis, start, i - 1)
    sort_list(lis, i + 1, end)


def find_peak(list_of_integers):
    """ return the pick of an lis of integer """
    size = len(list_of_integers)
    if size > 0:
        sort_list(list_of_integers, 0, size - 1)
        return list_of_integers[-1]
    else:
        return None
