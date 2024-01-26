#!/usr/bin/python3
""" find peak element """


def find_peak(list_of_integers):
	""" finds a peak in a list of unsorted integers. """
	length = len(list_of_integers)
	if (length == 0):
		return None
	if (length == 1):
		return list_of_integers[0]
	return find_peak_recursive(list_of_integers, 0, length - 1)


def find_peak_recursive(integers, low, high):
	""" recursive find_peak """

	if (low == high):
		return integers[low]

	mid = (low + high) // 2

	if (integers[mid] >= integers[mid + 1] and integers[mid] >= integers[mid - 1]):
		return integers[mid]
	elif (integers[mid] < integers[mid + 1]):
		return find_peak_recursive(integers, mid + 1, high)
	else:
		return find_peak_recursive(integers, low, mid - 1)

