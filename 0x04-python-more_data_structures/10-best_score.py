#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxKey, maxVal = "", 0
        for key, value in a_dictionary.items():
            if value > maxVal:
                maxVal = value
                maxKey = key
        return maxKey
    return None
