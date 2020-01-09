#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as exep:
        print("Exception: {}".format(exep), file=stderr)
        return (None)
