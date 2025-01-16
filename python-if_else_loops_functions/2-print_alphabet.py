#!/usr/bin/python3
def print_alphabet():
    c = 'a'
    while c <= 'z':
        print(c, end='')
        c = chr(ord(c) + 1)
    print()
