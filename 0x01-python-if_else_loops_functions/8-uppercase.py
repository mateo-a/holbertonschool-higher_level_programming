#!usr/bin/python3
def uppercase(str):
    print(''.join(['{}'.format(chr(ord(i) - 32)) if 122 >= ord(i) >= 97
                   else i for i in str]))
