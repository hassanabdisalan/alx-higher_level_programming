#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and isinstance(a_dictionary, dict):
        return max(a_dictionary, key=a_dictionary.get)
    return None
