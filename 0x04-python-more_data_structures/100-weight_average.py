#!/usr/bin/python3


def weight_average(my_list=[]):
    calc = 0
    if my_list:
        calc = sum(x[0] * x[1] for x in my_list)/sum(x[1] for x in my_list)
    return (calc)
