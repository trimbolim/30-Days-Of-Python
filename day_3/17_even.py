#!/usr/bin/python3

while True:
    num = int(input("Your number: "))
    if ((num % 2) == 0):
        print ("Your number {0} is even.".format(num))
    else:
        print ("Your number {0} is odd.".format(num))

