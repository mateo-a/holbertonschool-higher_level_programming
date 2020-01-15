#!/usr/bin/python3
def magic_string(strn=[0]):
    strn[0] += 1
    return(", ".join(["Holberton" for i in range(strn[0])]))