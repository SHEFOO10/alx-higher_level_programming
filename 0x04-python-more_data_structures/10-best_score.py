#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = max(list(a_dictionary.values()))
    for item in a_dictionary.items():
        if (item[1] == max_score):
            return item[0]
