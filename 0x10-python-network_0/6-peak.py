#!/usr/bin/python3


def find_peak(list_of_integers):
    '''Function that finds a peak in a list of unsorted integers'''
    length = len(list_of_integers)
    if length == 0:
        return(None)
    middle = length // 2
    if (middle == length - 1 or
            list_of_integers[middle] >= list_of_integers[middle + 1]) and\
            (middle == 0 or list_of_integers[middle] >=
                list_of_integers[middle - 1]):
        return list_of_integers[middle]
    if middle != length - 1 and list_of_integers[middle + 1] >\
            list_of_integers[middle]:
        return find_peak(list_of_integers[middle + 1:])
    return find_peak(list_of_integers[:middle])
