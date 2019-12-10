#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
if last > 5:
    msg = "and is greater than 5"
elif last != 0:
    msg = "and is less than 6 and not 0"
else:
    msg = "and is 0"
print("Last digit of", "{:d}".format(number), "is {:d}".format(last), msg)
