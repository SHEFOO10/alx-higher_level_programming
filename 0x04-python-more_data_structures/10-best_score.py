#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = sorted(
        a_dictionary.items(),
        key=lambda item: item[1], reverse=True)
    return max_score[0][0]
