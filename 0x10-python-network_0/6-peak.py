#!/usr/bin/python3


def find_peak(list_of_integers):
	""" return the pick of an lis of integer """

	if len(list_of_integers) > 0:
		peacks = []
		integers = list_of_integers.copy()
		for idx, num in enumerate(integers[1:-1]):
			if integers[idx - 1] <= num and num >= integers[idx + 1]:
				peacks.append(num)
		return max(peacks)
