#!/usr/bin/python3
def uppercase(str):
    for i in str:
        temp_file = i
        if ord(temp_file) >= 'a' and ord(temp_file) <= 'z':
            temp_file = temp_file + chr(ord(i - 32))
            print("{}".format(temp_file), end='')
    print()
