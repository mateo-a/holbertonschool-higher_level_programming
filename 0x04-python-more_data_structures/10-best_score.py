#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    sort_k = sorted(a_dictionary.keys(), key=lambda x: a_dictionary[x],
                         reverse=True)
    return (sort_k[0])
