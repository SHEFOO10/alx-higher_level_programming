#!/usr/bin/python3
def remove_char_at(str, n):
	str1 = ''
	if (n > len(str)):
		return str
	else:
		for i in range(len(str)):
			if (i != n):
			    str1 += str[i]
	return str1
